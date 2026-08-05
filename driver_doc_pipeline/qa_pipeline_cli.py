"""Driver-doc Q&A training pipeline CLI.

Usage examples (run from the driver_doc_pipeline folder):

    python qa_pipeline_cli.py convert --driver delimited
    python qa_pipeline_cli.py convert                # all drivers
    python qa_pipeline_cli.py generate --driver delimited
    python qa_pipeline_cli.py generate --auto-approve-cache-hits
    python qa_pipeline_cli.py status
    python qa_pipeline_cli.py drivers
"""
from __future__ import annotations

from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from qa_pipeline import cache, converter, progress, review, utils

app = typer.Typer(add_completion=False, help="NetIQ driver-doc Q&A training pipeline.")
console = Console()


@app.command()
def drivers() -> None:
    """List discovered driver slugs (from Driver_Docs_* folders)."""
    slugs = utils.discover_driver_slugs()
    table = Table(title=f"{len(slugs)} driver(s)")
    table.add_column("Slug", style="cyan")
    table.add_column("Display name", style="white")
    table.add_column("HTML files", justify="right")
    table.add_column("MD files", justify="right")
    for s in slugs:
        table.add_row(
            s,
            utils.driver_display_name(s),
            str(len(utils.list_html_files(s))),
            str(len(utils.list_markdown_files(s))),
        )
    console.print(table)


@app.command()
def convert(
    driver: Optional[List[str]] = typer.Option(
        None, "--driver", "-d", help="Driver slug(s) to convert. Omit for all."
    ),
    force: bool = typer.Option(False, "--force", help="Reconvert even if .md exists."),
) -> None:
    """Stage 1: convert driver HTML docs to Markdown."""
    converter.convert_all(drivers=driver or None, force=force)
    console.print("[bold green]Conversion done.[/bold green]")


@app.command()
def generate(
    driver: Optional[List[str]] = typer.Option(
        None, "--driver", "-d", help="Driver slug(s) to process. Omit for all."
    ),
    auto_approve_cache_hits: bool = typer.Option(
        False, "--auto-approve-cache-hits", help="Auto-approve files already in the cache."
    ),
    process_boilerplate: bool = typer.Option(
        False, "--process-boilerplate", help="Also process Legal Notice / Messages pages."
    ),
) -> None:
    """Stage 2: interactively generate + review Q&A, resuming from progress."""
    review.run(
        drivers=driver or None,
        auto_approve_cache_hits=auto_approve_cache_hits,
        skip_boilerplate=not process_boilerplate,
    )


@app.command()
def status() -> None:
    """Show conversion/approval progress and cache size."""
    cache.init_db()
    state = progress.load()
    table = Table(title="Pipeline status")
    table.add_column("Driver", style="cyan")
    table.add_column("Converted", justify="center")
    table.add_column("Approved", justify="right", style="green")
    table.add_column("Skipped", justify="right", style="yellow")
    table.add_column("Pending", justify="right", style="red")

    for slug in utils.discover_driver_slugs():
        entry = state.get(slug, {})
        files = entry.get("files", {})
        md_total = len(utils.list_markdown_files(slug))
        approved = sum(1 for v in files.values() if v == progress.APPROVED)
        skipped = sum(1 for v in files.values() if v == progress.SKIPPED)
        done = approved + skipped
        pending = max(md_total - done, 0)
        table.add_row(
            slug,
            "yes" if entry.get("converted") else "no",
            str(approved),
            str(skipped),
            str(pending),
        )
    console.print(table)
    console.print(f"[bold]Cached Q&A entries:[/bold] {cache.count_cached()}")


if __name__ == "__main__":
    app()
