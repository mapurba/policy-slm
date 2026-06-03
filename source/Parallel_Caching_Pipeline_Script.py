import os
import json
import logging
import sqlite3
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import boto3
from botocore.config import Config

# 📁 File and Database Configurations
INDEX_FILE = "/Users/ayoshi/Documents/source/policy-slm/policies_unique/index.json"
POLICIES_DIR = os.path.dirname(INDEX_FILE)

# Explicit absolute paths for outputs
OUTPUT_FILE = "/Users/ayoshi/Documents/source/policy-slm/train.jsonl"
DB_FILE = "/Users/ayoshi/Documents/source/policy-slm/policy_cache.db"
LOG_FILE = "/Users/ayoshi/Documents/source/policy-slm/pipeline.log"

# 🔒 Threading Lock for File and DB operations
pipeline_lock = threading.Lock()

# 📝 Configure Python Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (Thread-%(thread)d) %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# ☁️ Configure AWS Bedrock Client
bedrock_config = Config(retries={'max_attempts': 5, 'mode': 'standard'}, read_timeout=60)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1", config=bedrock_config)
MODEL_ID = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

SYSTEM_PROMPT = """You are an expert NetIQ DirXML developer. Analyze the provided XML and return a valid JSON object matching this schema exactly. Do not include markdown or conversational text.
{
  "explanation": "Natural English summary of logic",
  "generation_prompt": "Concise prompt to generate this exact XML",
  "broken_xml": "The XML broken by a DTD violation",
  "debugging_explanation": "Explanation of the fix and the corrected XML"
}"""

def clean_json_text(text):
    """🧹 Removes markdown code fences if present in the LLM response."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0]
    return text.strip()

def init_db():
    """🔨 Initializes the SQLite database and creates the cache table."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS policy_cache (
                checksum TEXT PRIMARY KEY,
                explanation TEXT,
                generation_prompt TEXT,
                broken_xml TEXT,
                debugging_explanation TEXT
            )
        """)
        conn.commit()

def check_cache(checksum):
    """🔍 Checks if the parsed LLM output already exists for a given checksum."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT explanation, generation_prompt, broken_xml, debugging_explanation FROM policy_cache WHERE checksum = ?", (checksum,))
        row = cursor.fetchone()
        if row:
            return {
                "explanation": row[0],
                "generation_prompt": row[1],
                "broken_xml": row[2],
                "debugging_explanation": row[3]
            }
    return None

def write_to_dataset_and_cache(checksum, data, xml_content):
    """💾 Thread-safe operation to save results to both the JSONL file and SQLite DB."""
    tasks = [
        {"instruction": data["generation_prompt"], "output": xml_content},
        {"instruction": "Explain the business logic of this DirXML policy.", "input": xml_content, "output": data["explanation"]},
        {"instruction": "Fix the syntax errors in this DirXML policy based on the DTD.", "input": data["broken_xml"], "output": data["debugging_explanation"]}
    ]
    
    with pipeline_lock:
        # Append to JSONL
        with open(OUTPUT_FILE, 'a', encoding='utf-8') as outfile:
            for task in tasks:
                outfile.write(json.dumps(task, ensure_ascii=False) + "\n")
        
        # Save to SQLite Cache
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO policy_cache (checksum, explanation, generation_prompt, broken_xml, debugging_explanation)
                VALUES (?, ?, ?, ?, ?)
            """, (checksum, data["explanation"], data["generation_prompt"], data["broken_xml"], data["debugging_explanation"]))
            conn.commit()

def process_single_policy(policy_info):
    """⚙️ Logic for a single policy file: Checks cache, falls back to Bedrock if missing."""
    filename = policy_info["filename"]
    policy_id = policy_info["id"]
    checksum = policy_info.get("checksum")
    file_path = os.path.join(POLICIES_DIR, filename)
    
    if not checksum:
        logging.warning(f"⚠️ Missing checksum for ID: {policy_id}. Skipping file.")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()

        # Check Cache Layer
        cached_data = check_cache(checksum)
        if cached_data:
            logging.info(f"🎯 Cache Hit for ID: {policy_id} (Checksum: {checksum[:8]}...). Appending to dataset.")
            write_to_dataset_and_cache(checksum, cached_data, xml_content)
            return True

        # Cache Miss -> Call AWS Bedrock
        logging.info(f"🌐 Cache Miss for ID: {policy_id}. Fetching from AWS Bedrock...")
        response = bedrock_client.converse(
            modelId=MODEL_ID,
            system=[{"text": SYSTEM_PROMPT}],
            messages=[{"role": "user", "content": [{"text": xml_content}]}]
        )
        
        response_text = response['output']['message']['content'][0]['text']
        cleaned_text = clean_json_text(response_text)
        data = json.loads(cleaned_text)
        
        # Commit to both files
        write_to_dataset_and_cache(checksum, data, xml_content)
        logging.info(f"✅ Successfully processed and cached ID: {policy_id}")
        return True

    except Exception as e:
        logging.error(f"❌ Error processing ID: {policy_id} | File: {filename} | Error: {str(e)}")
        return False

def parallel_pipeline(run_limit=10, max_workers=5):
    """🚀 Prepares the dataset loop and restricts execution to the specified limit."""
    init_db()
    
    if not os.path.exists(INDEX_FILE):
        logging.error(f"Index file missing at {INDEX_FILE}")
        return

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    policies = index_data.get("policies", [])
    
    # Slice the list to target exactly the first 10 items for this pilot test
    test_batch = policies[:run_limit]
    logging.info(f"📊 Starting pilot batch execution. Processing the first {len(test_batch)} policies.")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_policy, p): p for p in test_batch}
        for future in as_completed(futures):
            future.result()

    logging.info(f"🏁 Pilot run complete. Check {OUTPUT_FILE} and {DB_FILE} to verify outputs.")

if __name__ == "__main__":
    parallel_pipeline(run_limit=1987, max_workers=20)