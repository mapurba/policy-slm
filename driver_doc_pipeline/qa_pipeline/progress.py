"""Resumable progress tracking per driver/file.

Progress JSON shape:
{
  "<driver>": {
    "converted": true,
    "files": { "NNN_Title.md": "pending|approved|skipped|cache-hit" }
  }
}
"""
from __future__ import annotations

import json
import os
from typing import Dict

from . import config

PENDING = "pending"
APPROVED = "approved"
SKIPPED = "skipped"
CACHE_HIT = "cache-hit"


def load() -> Dict:
    if os.path.exists(config.PROGRESS_FILE):
        with open(config.PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(state: Dict) -> None:
    os.makedirs(os.path.dirname(config.PROGRESS_FILE), exist_ok=True)
    with open(config.PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def ensure_driver(state: Dict, driver: str) -> Dict:
    entry = state.setdefault(driver, {"converted": False, "files": {}})
    entry.setdefault("files", {})
    entry.setdefault("converted", False)
    return entry


def mark_converted(state: Dict, driver: str) -> None:
    ensure_driver(state, driver)["converted"] = True


def set_file_status(state: Dict, driver: str, filename: str, status: str) -> None:
    ensure_driver(state, driver)["files"][filename] = status


def get_file_status(state: Dict, driver: str, filename: str) -> str:
    return ensure_driver(state, driver)["files"].get(filename, PENDING)


def is_done(status: str) -> bool:
    """A file is 'done' (no more work) when approved or skipped."""
    return status in (APPROVED, SKIPPED)
