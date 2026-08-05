"""Shared configuration and paths for the driver-doc Q&A pipeline."""
from __future__ import annotations

import os

# 📁 Base directory = the driver_doc_pipeline folder (parent of this package)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Existing HTML docs live in Driver_Docs_<driver>/ folders under BASE_DIR
HTML_FOLDER_PREFIX = "Driver_Docs_"

# Stage 1 output: markdown/<driver>/NNN_Title.md
MARKDOWN_DIR = os.path.join(BASE_DIR, "markdown")

# Stage 2 review files: qa_review/<driver>/NNN_Title.qa.json
QA_REVIEW_DIR = os.path.join(BASE_DIR, "qa_review")

# Final approved training data (kept SEPARATE from dtd/policy data)
TRAINING_DIR = os.path.join(BASE_DIR, "training_data")
TRAINING_FILE = os.path.join(TRAINING_DIR, "driver_docs_train.jsonl")

# SQLite cache of generated Q&A keyed by markdown content hash
CACHE_DB = os.path.join(BASE_DIR, "driver_docs_cache.db")

# Resume state per driver/file
PROGRESS_FILE = os.path.join(BASE_DIR, "driver_docs_progress.json")

# Log file
LOG_FILE = os.path.join(BASE_DIR, "driver_docs_pipeline.log")

# ☁️ AWS Bedrock
MODEL_ID = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
AWS_REGION = "us-east-1"

# Filenames to skip by default (boilerplate that repeats across drivers)
SKIP_FILENAME_PATTERNS = ("legal_notice", "messages")

# System prompt for Q&A generation. The schema is enforced explicitly.
QA_SYSTEM_PROMPT = """You are an expert NetIQ (Micro Focus) Identity Manager engineer creating instruction-tuning data for a specialized assistant.
You will be given the Markdown content of ONE documentation page belonging to a specific NetIQ IDM driver, plus a driver-name hint.

Your job: produce high-quality question/answer pairs grounded ONLY in the provided page content.
Return a SINGLE valid JSON object matching this schema EXACTLY. No markdown fences, no commentary, no trailing text.

{
  "driver": "<canonical driver name, e.g. 'Delimited Text driver', 'JDBC driver', 'SAP HR driver'>",
  "qa_pairs": [
    {
      "category": "explanatory | howto | config | troubleshooting | summarization | grounded",
      "instruction": "<the question, natural and self-contained>",
      "input": "",
      "output": "<the answer, accurate and self-contained>"
    }
  ]
}

DRIVER NAME
- The hint you are given may be a rough slug (e.g. 'Sap Hr'). Infer the CANONICAL product name from the page content
  (e.g. 'SAP HR driver', 'Delimited Text driver', 'JDBC Fan-Out driver') and use it consistently in the "driver" field.
- CRITICAL: EVERY instruction AND EVERY output MUST explicitly name this driver, so each pair is self-identifying out of context.
  Prefer natural phrasing like "...in the Delimited Text driver" or "For the JDBC driver, ...". Never rely on pronouns like "it" or "this driver" alone.

COVERAGE (adaptive)
- Produce as many pairs as the page genuinely supports: a thin page may yield 1-3; a rich page 10+.
- Use ONLY these categories, and ONLY when the content truly supports them:
  1. explanatory   - what a concept/feature is and why it exists.
  2. howto         - concrete step-by-step procedures (preserve the real steps and order).
  3. config        - specific driver properties, GCVs, parameters, and their meanings/valid values.
  4. troubleshooting - a concrete problem and its documented resolution.
  5. summarization - one concise summary of the page's key points.
  6. grounded      - ONLY when the page actually shows a policy rule, style sheet, XSLT, or code; ask the model to write/produce that artifact and give the artifact as the answer.
- Vary the question wording (avoid starting every question with "What is"). Mix "How do you...", "Which...", "When should...", "Why does...".

FIDELITY
- Do NOT invent facts, property names, versions, or steps not present in the page. Copy exact property/GCV/attribute names verbatim.
- Preserve tables and configuration values precisely when answering config questions.
- If the page is pure navigation, a table of contents, a legal notice, or otherwise has no substantive content, return {"driver": "<name>", "qa_pairs": []}.
- Keep answers free of navigation links, breadcrumbs, image placeholders, and boilerplate.
"""

