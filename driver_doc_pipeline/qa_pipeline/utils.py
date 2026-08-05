"""Shared helpers: logging, hashing, driver discovery, JSON parsing."""
from __future__ import annotations

import hashlib
import logging
import os
import re
from typing import List

from . import config


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(config.LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def content_hash(text: str) -> str:
    """Stable sha256 over the markdown content (used as the cache key)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_json_text(text: str) -> str:
    """Strip markdown code fences if the LLM wrapped its JSON output."""
    text = (text or "").strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0]
    return text.strip()


def driver_display_name(driver_slug: str) -> str:
    """Turn a folder slug like 'bi_impl_mf-racf' into a readable driver name."""
    name = driver_slug.replace("_", " ").replace("-", " ").strip()
    return re.sub(r"\s+", " ", name).title()


def html_folder_for(driver_slug: str) -> str:
    return os.path.join(config.BASE_DIR, f"{config.HTML_FOLDER_PREFIX}{driver_slug}")


def markdown_folder_for(driver_slug: str) -> str:
    return os.path.join(config.MARKDOWN_DIR, driver_slug)


def review_folder_for(driver_slug: str) -> str:
    return os.path.join(config.QA_REVIEW_DIR, driver_slug)


def discover_driver_slugs() -> List[str]:
    """Find all Driver_Docs_<driver> folders, returning sorted driver slugs."""
    slugs = []
    for entry in os.listdir(config.BASE_DIR):
        full = os.path.join(config.BASE_DIR, entry)
        if os.path.isdir(full) and entry.startswith(config.HTML_FOLDER_PREFIX):
            slugs.append(entry[len(config.HTML_FOLDER_PREFIX):])
    return sorted(slugs)


def list_html_files(driver_slug: str) -> List[str]:
    """Return sorted NNN_*.html filenames for a driver."""
    folder = html_folder_for(driver_slug)
    if not os.path.isdir(folder):
        return []
    return sorted(f for f in os.listdir(folder) if f.lower().endswith(".html"))


def list_markdown_files(driver_slug: str) -> List[str]:
    """Return sorted NNN_*.md filenames for a driver."""
    folder = markdown_folder_for(driver_slug)
    if not os.path.isdir(folder):
        return []
    return sorted(f for f in os.listdir(folder) if f.lower().endswith(".md"))


def should_skip_filename(filename: str) -> bool:
    """True if the file matches a boilerplate skip pattern (legal, messages)."""
    lower = filename.lower()
    return any(pat in lower for pat in config.SKIP_FILENAME_PATTERNS)
