# Plan: Driver-Doc Q&A Training Pipeline

Build a resumable, interactive Typer CLI that converts each driver's HTML docs to Markdown (via Microsoft **MarkItDown**), then generates **driver-tagged Q&A** from AWS Bedrock Claude Sonnet 4.5 — one driver at a time, one file at a time — with a review-then-approve step, SQLite caching, and separate training output. Everything stays in Python and mirrors your existing `Parallel_Caching_Pipeline_Script.py` patterns.

## Phases

### Phase 1 — HTML → Markdown (deterministic, resumable)
1. `convert` command iterates `Driver_Docs_<driver>/NNN_*.html` and writes `markdown/<driver>/NNN_*.md` using `MarkItDown().convert(path).text_content`. Skips files already converted (idempotent). Rich progress bar. *(Stage 1 can run standalone)*

### Phase 2 — Interactive Q&A generation *(depends on Phase 1)*
2. `generate` command walks drivers in order, then md files in `NNN` order, starting at the first pending file.
3. Per file: compute sha256 hash → **cache check** in SQLite. Cache miss → call Bedrock `converse` with a schema-locked system prompt → parse via `clean_json_text` → write pretty JSON to `qa_review/<driver>/<file>.qa.json`.
4. CLI prompts `[ok / skip / redo / quit]`:
   - **ok** → re-read the (edited) review file, validate, cache to SQLite, append flattened records to `training_data/driver_docs_train.jsonl`, mark `approved`.
   - **redo** → re-call Bedrock; **skip** → mark skipped; **quit** → persist progress and exit cleanly.
5. Resume: `driver_docs_progress.json` tracks `pending|approved|skipped` per file so it continues after shutdown.

## Q&A schema (adaptive count, 6 categories)
Explanatory, How-to, Config lookup, Troubleshooting, Summarization, Grounded-generation — **every question and answer embeds the driver name**; grounded-generation only when the doc actually shows a rule/stylesheet.

```json
{
  "driver": "<driver display name>",
  "qa_pairs": [
    {
      "category": "explanatory|howto|config|troubleshooting|summarization|grounded",
      "instruction": "<question, includes driver name>",
      "input": "",
      "output": "<answer, includes driver name>"
    }
  ]
}
```

- System prompt instructs: adaptive count, 6 categories only when content supports, EVERY question + answer must name the driver, grounded-generation only when the doc actually shows a rule/stylesheet.
- Final training records flatten `qa_pairs` → `{"instruction","input"(if any),"output"}` appended to JSONL.

## Decisions (from user)
- HTML→MD: **Microsoft MarkItDown** (Python lib) `pip install 'markitdown[all]'`, API `MarkItDown().convert(path).text_content`.
- CLI: **Typer + Rich**.
- Approval: edit temp file, then type `ok`/`skip`/`redo`/`quit` at the running CLI prompt (per file).
- Model: **us.anthropic.claude-sonnet-4-5-20250929-v1:0** (same as `Parallel_Caching_Pipeline_Script.py`).
- Q&A count: **adaptive** (LLM decides based on content).
- Every Q AND A must embed the driver name for correlation.

## Existing structures to reuse
- Bedrock pattern + SQLite cache + `clean_json_text`: `source/Parallel_Caching_Pipeline_Script.py` (converse API, retries `Config`, `INSERT OR REPLACE` cache, `pipeline_lock`, `clean_json_text`).
- Driver folders: `driver_doc_pipeline/Driver_Docs_<driver>/NNN_Title.html` (~1584 html files, 41 drivers).
- Driver list source: `driver_doc_pipeline/driver_doc_links.json` (driver name = url part `[-3]`).
- Task record shape for training JSONL: `{"instruction":..., "input"?:..., "output":...}` (matches `train.jsonl`).

## Target layout (all under `driver_doc_pipeline/`)
- `Driver_Docs_<driver>/`          — existing HTML (leave as-is; treat as the "html" set)
- `markdown/<driver>/NNN_Title.md` — Stage 1 output
- `qa_review/<driver>/NNN_Title.qa.json` — temp review file (user edits)
- `training_data/driver_docs_train.jsonl` — final approved Q&A (SEPARATE from dtd/policy)
- `driver_docs_cache.db`           — SQLite cache (question+answer by content hash)
- `driver_docs_progress.json`      — resume state per driver/file
- `driver_docs_pipeline.log`

## SQLite schema (`driver_docs_cache.db`)
```sql
qa_cache(content_hash TEXT PRIMARY KEY, driver TEXT, source_file TEXT, qa_json TEXT, created_at TEXT)
```

## Progress schema (`driver_docs_progress.json`)
```json
{ "<driver>": { "converted": true, "files": { "NNN_Title.md": "pending|approved|skipped|cache-hit" } } }
```

## Relevant files
- `source/Parallel_Caching_Pipeline_Script.py` — reuse Bedrock `converse`, retry `Config`, `INSERT OR REPLACE` cache, `clean_json_text`.
- `driver_doc_pipeline/download_driverDoc.py` — reuse driver-name derivation + slug logic.
- `train.jsonl` / `training_data/*.jsonl` — training record shape reference (keep NEW file separate).
- `requirements.txt` — add `markitdown[all]`, `typer`, `rich`.

## Verification
1. Run `convert --driver delimited`; confirm `markdown/delimited/*.md` count == html count; spot-check one md.
2. Run `generate --driver delimited`; confirm a `.qa.json` review file is written, prompt appears.
3. Edit review file, type `ok`; confirm row added to SQLite (`SELECT count(*)`), records appended to `driver_docs_train.jsonl` with driver name present in every instruction + output.
4. Type `quit`, re-run `generate`; confirm it resumes at the next pending file (no re-processing approved).
5. Re-run a file whose hash is cached; confirm cache-hit path (no Bedrock call) via log.
6. Validate JSONL: every line parses; every record has driver name in instruction and output.

## Scope
- **Included:** Stage 1 converter, Stage 2 interactive generator, SQLite cache, resumable progress, separate JSONL, Typer CLI.
- **Excluded:** merging driver-docs JSONL into the tag/policy curriculum (separate later step); notebook training changes; re-downloading HTML (already present).

## Open considerations
1. **Boilerplate/near-duplicate pages** (install/upgrade/legal repeat across drivers). Dedup by content hash in cache naturally reuses answers, but still appends per-driver records. Recommend: keep per-driver (driver name differs) but SKIP legal/notice pages by filename filter (auto-skip `*Legal_Notice*`, `*Messages*`). Option A: auto-skip / Option B: process everything.
2. **Batch approve for cache-hits** — offer `--auto-approve-cache-hits` flag to speed resumes. Recommend: yes.
