"""Stage 2 orchestration: interactive, resumable Q&A review per driver/file."""
from __future__ import annotations

import json
import logging
import os
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from . import cache, config, generator, progress, utils

console = Console()


def _write_review_file(driver_slug: str, md_name: str, qa_payload: Dict) -> str:
    folder = utils.review_folder_for(driver_slug)
    os.makedirs(folder, exist_ok=True)
    review_path = os.path.join(folder, os.path.splitext(md_name)[0] + ".qa.json")
    with open(review_path, "w", encoding="utf-8") as f:
        json.dump(qa_payload, f, indent=2, ensure_ascii=False)
    return review_path


def _read_review_file(review_path: str) -> Dict:
    with open(review_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _append_training_records(records: List[Dict]) -> None:
    os.makedirs(config.TRAINING_DIR, exist_ok=True)
    with open(config.TRAINING_FILE, "a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _summarize_payload(qa_payload: Dict, source: str) -> None:
    table = Table(title=f"Q&A draft ({source})", show_lines=False)
    table.add_column("#", justify="right", style="cyan", no_wrap=True)
    table.add_column("Category", style="magenta")
    table.add_column("Question", style="white")
    for idx, p in enumerate(qa_payload.get("qa_pairs", []), 1):
        q = p.get("instruction", "")
        table.add_row(str(idx), p.get("category", ""), (q[:90] + "…") if len(q) > 90 else q)
    console.print(table)


def _approve(driver_slug: str, md_name: str, review_path: str, content_hash: str,
             driver_display: str, state: Dict) -> int:
    """Read (possibly edited) review file, cache it, append records. Returns count."""
    payload = _read_review_file(review_path)
    warnings = generator.validate_driver_tagging(payload)
    for w in warnings:
        console.print(f"[yellow]⚠ {w}[/yellow]")

    records = generator.flatten_to_records(payload)
    if not records:
        console.print("[yellow]No Q&A pairs to write; marking approved anyway.[/yellow]")
    cache.put_cached(content_hash, driver_display, md_name, json.dumps(payload, ensure_ascii=False))
    _append_training_records(records)
    progress.set_file_status(state, driver_slug, md_name, progress.APPROVED)
    progress.save(state)
    return len(records)


def _process_file(driver_slug: str, md_name: str, driver_display: str, state: Dict,
                  auto_approve_cache_hits: bool) -> str:
    """Handle one markdown file interactively. Returns 'continue' or 'quit'."""
    md_path = os.path.join(utils.markdown_folder_for(driver_slug), md_name)
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read().strip()

    if not md_text:
        console.print(f"[dim]{driver_slug}/{md_name}: empty markdown, skipping.[/dim]")
        progress.set_file_status(state, driver_slug, md_name, progress.SKIPPED)
        progress.save(state)
        return "continue"

    chash = utils.content_hash(md_text)
    cached_json = cache.get_cached(chash)
    source = "cache-hit" if cached_json else "bedrock"

    if cached_json:
        payload = json.loads(cached_json)
        logging.info("Cache hit for %s/%s", driver_slug, md_name)
    else:
        console.print(f"[cyan]Generating Q&A for {driver_slug}/{md_name} via Bedrock…[/cyan]")
        try:
            payload = generator.generate_qa(driver_display, md_text)
        except Exception as exc:  # noqa: BLE001
            logging.error("Generation failed for %s/%s: %s", driver_slug, md_name, exc)
            console.print(f"[red]Generation failed: {exc}. Skipping this file.[/red]")
            progress.set_file_status(state, driver_slug, md_name, progress.SKIPPED)
            progress.save(state)
            return "continue"

    review_path = _write_review_file(driver_slug, md_name, payload)

    console.print(Panel.fit(
        f"[bold]{driver_slug}/{md_name}[/bold]\nReview file: [green]{review_path}[/green]",
        title=f"{source}",
    ))
    _summarize_payload(payload, source)

    if source == "cache-hit" and auto_approve_cache_hits:
        n = _approve(driver_slug, md_name, review_path, chash, driver_display, state)
        console.print(f"[green]Auto-approved cache hit: {n} record(s) appended.[/green]")
        return "continue"

    while True:
        console.print(
            "\n[bold]Edit the review file if needed, then choose:[/bold] "
            "[green]ok[/green] / [yellow]skip[/yellow] / [cyan]redo[/cyan] / [red]quit[/red]"
        )
        choice = Prompt.ask("Action", choices=["ok", "skip", "redo", "quit"], default="ok")

        if choice == "ok":
            n = _approve(driver_slug, md_name, review_path, chash, driver_display, state)
            console.print(f"[green]Approved: {n} record(s) appended to training data.[/green]")
            return "continue"
        if choice == "skip":
            progress.set_file_status(state, driver_slug, md_name, progress.SKIPPED)
            progress.save(state)
            console.print("[yellow]Skipped.[/yellow]")
            return "continue"
        if choice == "quit":
            console.print("[red]Quitting. Progress saved; rerun to resume.[/red]")
            return "quit"
        if choice == "redo":
            guidance = Prompt.ask("Optional guidance for regeneration", default="")
            console.print("[cyan]Regenerating via Bedrock…[/cyan]")
            try:
                payload = generator.generate_qa(driver_display, md_text, guidance=guidance)
            except Exception as exc:  # noqa: BLE001
                console.print(f"[red]Regeneration failed: {exc}[/red]")
                continue
            review_path = _write_review_file(driver_slug, md_name, payload)
            _summarize_payload(payload, "bedrock (redo)")


def run(drivers: Optional[List[str]] = None, auto_approve_cache_hits: bool = False,
        skip_boilerplate: bool = True) -> None:
    """Walk drivers/files in order, resuming from the first pending file."""
    utils.configure_logging()
    cache.init_db()
    state = progress.load()

    targets = drivers or utils.discover_driver_slugs()
    console.print(f"[bold]Processing {len(targets)} driver(s).[/bold]")

    for slug in targets:
        display = utils.driver_display_name(slug)
        md_files = utils.list_markdown_files(slug)
        if not md_files:
            console.print(f"[yellow]{slug}: no markdown yet. Run 'convert' first.[/yellow]")
            continue

        console.print(f"\n[bold underline]Driver: {display} ({slug})[/bold underline]")
        for md_name in md_files:
            status = progress.get_file_status(state, slug, md_name)
            if progress.is_done(status):
                continue
            if skip_boilerplate and utils.should_skip_filename(md_name):
                progress.set_file_status(state, slug, md_name, progress.SKIPPED)
                progress.save(state)
                console.print(f"[dim]{slug}/{md_name}: boilerplate, auto-skipped.[/dim]")
                continue

            result = _process_file(slug, md_name, display, state, auto_approve_cache_hits)
            if result == "quit":
                return

    console.print("[bold green]All drivers/files processed.[/bold green]")
