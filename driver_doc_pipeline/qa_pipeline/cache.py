"""SQLite cache for generated Q&A, keyed by markdown content hash."""
from __future__ import annotations

import datetime as _dt
import sqlite3
from typing import Optional

from . import config


def init_db() -> None:
    with sqlite3.connect(config.CACHE_DB) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS qa_cache (
                content_hash TEXT PRIMARY KEY,
                driver TEXT,
                source_file TEXT,
                qa_json TEXT,
                created_at TEXT
            )
            """
        )
        conn.commit()


def get_cached(content_hash: str) -> Optional[str]:
    """Return the cached qa_json string for a hash, or None."""
    with sqlite3.connect(config.CACHE_DB) as conn:
        row = conn.execute(
            "SELECT qa_json FROM qa_cache WHERE content_hash = ?", (content_hash,)
        ).fetchone()
    return row[0] if row else None


def put_cached(content_hash: str, driver: str, source_file: str, qa_json: str) -> None:
    with sqlite3.connect(config.CACHE_DB) as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO qa_cache
                (content_hash, driver, source_file, qa_json, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (content_hash, driver, source_file, qa_json, _dt.datetime.utcnow().isoformat()),
        )
        conn.commit()


def count_cached() -> int:
    with sqlite3.connect(config.CACHE_DB) as conn:
        return conn.execute("SELECT COUNT(*) FROM qa_cache").fetchone()[0]
