"""Bedrock-backed Q&A generation for a single markdown page."""
from __future__ import annotations

import json
import logging
from typing import Dict, List

import boto3
from botocore.config import Config

from . import config, utils

_bedrock_config = Config(
    retries={"max_attempts": 5, "mode": "standard"},
    connect_timeout=10,
    read_timeout=120,
)
_bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=config.AWS_REGION,
    config=_bedrock_config,
)

VALID_CATEGORIES = {
    "explanatory",
    "howto",
    "config",
    "troubleshooting",
    "summarization",
    "grounded",
}


def generate_qa(driver_display: str, markdown_text: str, guidance: str = "") -> Dict:
    """Call Bedrock and return a parsed {"driver","qa_pairs":[...]} dict.

    Raises on API or JSON errors so the caller can decide how to handle.
    """
    user_text = (
        f"Driver name: {driver_display}\n\n"
        f"{('Extra guidance: ' + guidance + chr(10) + chr(10)) if guidance else ''}"
        f"Documentation page (Markdown):\n\n{markdown_text}"
    )

    response = _bedrock_client.converse(
        modelId=config.MODEL_ID,
        system=[{"text": config.QA_SYSTEM_PROMPT}],
        messages=[{"role": "user", "content": [{"text": user_text}]}],
    )
    raw = response["output"]["message"]["content"][0]["text"]
    data = json.loads(utils.clean_json_text(raw))
    return _normalize(data, driver_display)


def _normalize(data: Dict, driver_display: str) -> Dict:
    """Ensure the payload has the expected shape and a driver field."""
    if not isinstance(data, dict):
        raise ValueError("LLM output was not a JSON object")
    data.setdefault("driver", driver_display)
    pairs = data.get("qa_pairs") or []
    if not isinstance(pairs, list):
        raise ValueError("'qa_pairs' must be a list")

    cleaned: List[Dict] = []
    for p in pairs:
        if not isinstance(p, dict):
            continue
        instruction = (p.get("instruction") or "").strip()
        output = (p.get("output") or "").strip()
        if not instruction or not output:
            continue
        category = (p.get("category") or "").strip().lower()
        if category not in VALID_CATEGORIES:
            category = "explanatory"
        cleaned.append(
            {
                "category": category,
                "instruction": instruction,
                "input": (p.get("input") or "").strip(),
                "output": output,
            }
        )
    data["qa_pairs"] = cleaned
    return data


def flatten_to_records(qa_payload: Dict) -> List[Dict]:
    """Flatten a qa payload into training records (instruction/input?/output)."""
    records = []
    for p in qa_payload.get("qa_pairs", []):
        rec = {"instruction": p["instruction"], "output": p["output"]}
        if p.get("input"):
            rec["input"] = p["input"]
        records.append(rec)
    return records


def validate_driver_tagging(qa_payload: Dict) -> List[str]:
    """Return a list of warnings for pairs missing the driver name in Q or A."""
    driver = (qa_payload.get("driver") or "").strip().lower()
    warnings: List[str] = []
    if not driver:
        return ["payload has no driver name"]
    # Match on any distinctive token from the driver name (handles 'the ... driver' phrasing).
    tokens = [t for t in driver.replace("driver", "").split() if len(t) > 2]
    for idx, p in enumerate(qa_payload.get("qa_pairs", [])):
        blob = (p.get("instruction", "") + " " + p.get("output", "")).lower()
        if tokens and not any(tok in blob for tok in tokens):
            warnings.append(f"pair #{idx + 1} may not mention the driver name")
    return warnings
