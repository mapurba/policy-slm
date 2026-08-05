"""Stage 1: convert driver HTML docs to Markdown using Microsoft MarkItDown."""
from __future__ import annotations

import logging
import os
from typing import List, Optional

from markitdown import MarkItDown

from . import config, progress, utils

_md = MarkItDown(enable_plugins=False)


def _repair_mojibake(text: str) -> str:
    """Fix classic UTF-8-decoded-as-Latin1 mojibake (e.g. 'donât' -> 'don't').

    NetIQ pages use UTF-8 smart punctuation; some get mis-decoded upstream,
    producing 'Ã¢â‚¬â„¢' style sequences. Round-tripping through latin-1 repairs them.
    """
    if "Ã" not in text and "â" not in text:
        return text
    try:
        repaired = text.encode("latin-1").decode("utf-8")
        return repaired
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def _convert_one(html_path: str) -> str:
    """Convert a single HTML file to markdown text."""
    result = _md.convert(html_path)
    return _repair_mojibake((result.text_content or "").strip())


def convert_driver(driver_slug: str, state: dict, force: bool = False) -> int:
    """Convert all HTML files for a driver into markdown/<driver>/*.md.

    Returns the number of files converted this run. Idempotent: existing .md
    files are skipped unless force=True.
    """
    html_files = utils.list_html_files(driver_slug)
    if not html_files:
        logging.warning("No HTML files found for driver '%s'", driver_slug)
        return 0

    src_folder = utils.html_folder_for(driver_slug)
    dst_folder = utils.markdown_folder_for(driver_slug)
    os.makedirs(dst_folder, exist_ok=True)

    converted = 0
    for html_name in html_files:
        md_name = os.path.splitext(html_name)[0] + ".md"
        md_path = os.path.join(dst_folder, md_name)
        if os.path.exists(md_path) and not force:
            continue
        try:
            text = _convert_one(os.path.join(src_folder, html_name))
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(text + "\n")
            converted += 1
            logging.info("Converted %s/%s", driver_slug, md_name)
        except Exception as exc:  # noqa: BLE001
            logging.error("Failed converting %s/%s: %s", driver_slug, html_name, exc)

    progress.mark_converted(state, driver_slug)
    return converted


def convert_all(drivers: Optional[List[str]] = None, force: bool = False) -> None:
    """Convert one or all drivers. Persists progress after each driver."""
    utils.configure_logging()
    os.makedirs(config.MARKDOWN_DIR, exist_ok=True)
    state = progress.load()

    targets = drivers or utils.discover_driver_slugs()
    logging.info("Converting %d driver(s) to markdown", len(targets))

    for slug in targets:
        n = convert_driver(slug, state, force=force)
        progress.save(state)
        logging.info("Driver '%s': %d file(s) converted", slug, n)

    logging.info("HTML -> Markdown conversion complete")
