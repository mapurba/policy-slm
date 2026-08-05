# Driver-Doc Q&A Training Pipeline

Generate instruction-tuning data for a NetIQ Identity Manager assistant from the official driver
documentation. The pipeline converts each driver's HTML docs to Markdown, then uses AWS Bedrock
(Claude Sonnet 4.5) to draft **driver-tagged question/answer pairs** — one driver at a time, one file
at a time — with a human review-and-approve step, an answer cache, and fully resumable progress.

The output is kept **separate** from the existing DTD/policy training data.

---

## Why this exists

The driver docs are prose/reference material (concepts, configuration, troubleshooting). Training on
raw docs makes a model *recite* pages. Instead, this pipeline turns each page into varied Q&A pairs
where **every question and answer names its driver**, so the model learns *which* driver a fact
belongs to and can *answer/apply* rather than parrot.

---

## Layout

```
driver_doc_pipeline/
├── qa_pipeline_cli.py            # CLI entry point (Typer)
├── qa_pipeline/                  # package
│   ├── config.py                 # paths, model id, skip patterns, the Q&A system prompt
│   ├── utils.py                  # logging, hashing, driver discovery, JSON cleaning
│   ├── cache.py                  # SQLite answer cache (keyed by markdown content hash)
│   ├── progress.py               # resumable per-driver/per-file status store
│   ├── converter.py              # Stage 1: HTML → Markdown (MarkItDown)
│   ├── generator.py              # Bedrock call + JSON normalization + validation
│   └── review.py                 # Stage 2: interactive review/approve loop
│
├── Driver_Docs_<driver>/         # INPUT: existing HTML docs (one folder per driver)
├── markdown/<driver>/*.md        # Stage 1 output
├── qa_review/<driver>/*.qa.json  # per-file draft you edit before approving
│
├── training_data/
│   └── driver_docs_train.jsonl   # OUTPUT: approved Q&A (separate from dtd/policy data)
├── driver_docs_cache.db          # SQLite cache of generated Q&A
├── driver_docs_progress.json     # resume state (see "Progress & resume")
└── driver_docs_pipeline.log      # run log
```

---

## Prerequisites

- Python 3.10+ and the project virtual environment.
- Dependencies (already in the repo `requirements.txt`): `markitdown[all]`, `typer`, `rich`,
  `boto3`, `botocore`.
- AWS credentials configured for Bedrock access in `us-east-1` (only needed for Stage 2).

Install / activate (Windows PowerShell):

```powershell
# from the repo root
& d:\gitlab\policy-slm\.venv\Scripts\Activate.ps1
uv pip install -r .\requirements.txt   # or: pip install -r requirements.txt
cd .\driver_doc_pipeline
```

> All commands below are run from inside `driver_doc_pipeline/` with the venv active.

---

## Commands

| Command | Purpose |
|---|---|
| `python qa_pipeline_cli.py drivers` | List discovered drivers with HTML/MD file counts. |
| `python qa_pipeline_cli.py convert` | **Stage 1** — convert HTML → Markdown (all drivers). |
| `python qa_pipeline_cli.py generate` | **Stage 2** — interactively draft/review/approve Q&A. |
| `python qa_pipeline_cli.py status` | Show per-driver Converted / Approved / Skipped / Pending + cache size. |

### Stage 1 — convert

```powershell
python qa_pipeline_cli.py convert                 # all drivers
python qa_pipeline_cli.py convert --driver delimited
python qa_pipeline_cli.py convert -d delimited -d jdbc
python qa_pipeline_cli.py convert --force         # re-convert even if .md exists
```

- Idempotent: existing `.md` files are skipped unless `--force`.
- Fixes common UTF-8 mojibake (e.g. `donât` → `don't`).

### Stage 2 — generate (interactive)

```powershell
python qa_pipeline_cli.py generate --driver delimited
python qa_pipeline_cli.py generate                        # all drivers, in order
python qa_pipeline_cli.py generate --auto-approve-cache-hits
python qa_pipeline_cli.py generate --process-boilerplate  # include Legal Notice / Messages
```

For each pending markdown file the tool:

1. Computes a content hash and checks the **cache**. On a cache hit it reuses the stored Q&A
   (no Bedrock call).
2. On a miss, calls Bedrock and drafts Q&A.
3. Writes the draft to `qa_review/<driver>/<file>.qa.json`, prints a summary table, and prompts:

   ```
   Action  [ok / skip / redo / quit]
   ```

   | Choice | Effect |
   |---|---|
   | `ok` | Re-reads the (edited) review file, caches it, appends records to `driver_docs_train.jsonl`, marks the file **approved**. |
   | `skip` | Marks the file **skipped** (no records written). |
   | `redo` | Re-calls Bedrock (optionally with extra guidance) and rewrites the draft. |
   | `quit` | Saves progress and exits cleanly — rerun to resume. |

**Review workflow:** when prompted, open the printed `*.qa.json`, edit questions/answers as needed,
save it, then type `ok`. Your edits (not the raw draft) are what get cached and written.

---

## Progress & resume

All state lives in a single file: **`driver_docs_progress.json`**.

```json
{
  "<driver-slug>": {
    "converted": true,
    "files": {
      "001_Understanding_....md": "approved",
      "002_How_....md": "skipped"
    }
  }
}
```

- `converted` — Stage 1 finished for that driver.
- `files[...]` — Stage 2 status per file: `approved`, `skipped` (both count as *done*), or `cache-hit`.
- A filename **absent** from `files` is treated as **pending**.

**How "next" is chosen (no stored pointer):** `generate` walks drivers in sorted order, then files in
`NNN` order, and processes the *first* file whose status isn't `approved`/`skipped`. Status is saved to
disk **immediately** after every action, so a shutdown loses at most the one in-flight file (which
simply reverts to pending and is regenerated).

Check anytime:

```powershell
python qa_pipeline_cli.py status
```

---

## Caching

`driver_docs_cache.db` (SQLite) stores approved Q&A keyed by the markdown content hash:

```
qa_cache(content_hash TEXT PK, driver TEXT, source_file TEXT, qa_json TEXT, created_at TEXT)
```

If the same content (identical hash) is seen again — including near-duplicate pages shared across
drivers — the cached Q&A is reused instead of calling Bedrock. Use `--auto-approve-cache-hits` to
fast-forward through cached files on resume.

---

## Output format

`training_data/driver_docs_train.jsonl` — one JSON record per line, matching the project's training
shape:

```json
{"instruction": "How do you set up one-way synchronization in the Delimited Text driver?", "output": "For the Delimited Text driver, ..."}
```

`input` is included only when a record needs extra context. Every record's `instruction` and `output`
are expected to name the driver (the generator warns if a pair appears not to).

---

## Configuration

Edit `qa_pipeline/config.py`:

- `MODEL_ID` / `AWS_REGION` — Bedrock model and region.
- `SKIP_FILENAME_PATTERNS` — filename substrings auto-skipped as boilerplate (default: `legal_notice`,
  `messages`). Override per run with `--process-boilerplate`.
- `QA_SYSTEM_PROMPT` — the generation instructions (categories, driver-tagging rules, fidelity rules).

---

## Typical run

```powershell
& d:\gitlab\policy-slm\.venv\Scripts\Activate.ps1
cd d:\gitlab\policy-slm\driver_doc_pipeline

python qa_pipeline_cli.py convert --driver delimited     # 1. HTML -> MD
python qa_pipeline_cli.py generate --driver delimited    # 2. draft, edit, approve per file
python qa_pipeline_cli.py status                         # 3. check progress anytime
```

Stop with `quit` whenever you like; rerun `generate` to continue from the next pending file.

---

## Scope

- **Included:** HTML→MD conversion, interactive Q&A generation, answer caching, resumable progress,
  separate training JSONL, Typer CLI.
- **Excluded:** merging `driver_docs_train.jsonl` into the tag/policy training curriculum (a later
  step), model fine-tuning, and re-downloading HTML (see `download_driverDoc.py`).
