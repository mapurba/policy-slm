import os
import json
import logging
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import boto3
from botocore.config import Config

# 📁 File Path Configurations
POLICIES_DIR = "./policies"
INDEX_FILE = "./policies/index.json"
OUTPUT_FILE = "train.jsonl"
MANIFEST_FILE = "processed_manifest.json"
LOG_FILE = "pipeline.log"

# ⚙️ Threading Lock for file writing
file_lock = threading.Lock()

# 📝 Configure Python Logger (Logs to both Console and File)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (Thread-%(thread)d) %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# ☁️ Configure AWS Bedrock Client with an aggressive retry/timeout policy for scaling
bedrock_config = Config(
    retries={'max_attempts': 5, 'mode': 'standard'},
    connect_timeout=10,
    read_timeout=60
)
bedrock_client = boto3.client(
    service_name="bedrock-runtime", 
    region_name="us-east-1", 
    config=bedrock_config
)
MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"

# 📜 System Prompt defining the structural source of truth
SYSTEM_PROMPT = """You are an expert NetIQ DirXML developer. Analyze the provided XML and return a valid JSON object matching this schema exactly. Do not include markdown or conversational text.
{
  "explanation": "Natural English summary of logic",
  "generation_prompt": "Concise prompt to generate this exact XML",
  "broken_xml": "The XML broken by a DTD violation",
  "debugging_explanation": "Explanation of the fix and the corrected XML"
}"""

def load_json_file(filepath, default_value):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default_value

def save_manifest(processed_set):
    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(processed_set), f, indent=2)

def process_single_policy(policy_info):
    filename = policy_info["filename"]
    policy_id = policy_info["id"]
    file_path = os.path.join(POLICIES_DIR, filename)
    
    try:
        logging.info(f"🚀 Starting processing for ID: {policy_id} | File: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
            
        # 🤖 AWS Bedrock API Call
        response = bedrock_client.converse(
            modelId=MODEL_ID,
            system=[{"text": SYSTEM_PROMPT}],
            messages=[{"role": "user", "content": [{"text": xml_content}]}]
        )
        
        response_text = response['output']['message']['content'][0]['text']
        data = json.loads(response_text)
        
        # 🛠️ Structure into the 3 distinct dataset training tasks
        tasks = [
            {"instruction": data["generation_prompt"], "output": xml_content},
            {"instruction": "Explain the business logic of this DirXML policy.", "input": xml_content, "output": data["explanation"]},
            {"instruction": "Fix the syntax errors in this DirXML policy based on the DTD.", "input": data["broken_xml"], "output": data["debugging_explanation"]}
        ]
        
        # 🔒 Thread-Safe Write Operations
        with file_lock:
            # Append tasks to training dataset
            with open(OUTPUT_FILE, 'a', encoding='utf-8') as outfile:
                for task in tasks:
                    outfile.write(json.dumps(task, ensure_ascii=False) + "\n")
            
            # Read, update, and save manifest state immediately to survive potential crashes
            current_manifest = set(load_json_file(MANIFEST_FILE, []))
            current_manifest.add(policy_id)
            save_manifest(current_manifest)
            
        logging.info(f"✅ Successfully completed and saved data for ID: {policy_id}")
        return True

    except Exception as e:
        logging.error(f"❌ Failed processing ID: {policy_id} | File: {filename} | Error: {str(e)}")
        return False

def parallel_pipeline(max_workers=10):
    logging.info("⚙️ Initializing pipeline architecture...")
    
    # 📑 Step 1: Load mapping and state manifest
    index_data = load_json_file(INDEX_FILE, {"policies": []})
    policies = index_data.get("policies", [])
    processed_manifest = set(load_json_file(MANIFEST_FILE, []))
    
    # 🎛️ Step 2: Filter out already processed files
    remaining_policies = [p for p in policies if p["id"] not in processed_manifest]
    
    total_count = len(policies)
    skipped_count = total_count - len(remaining_policies)
    logging.info(f"📊 Dataset Summary: Total={total_count} | Already Processed (Skipped)={skipped_count} | Queue Remaining={len(remaining_policies)}")
    
    if not remaining_policies:
        logging.info("🏁 All policies have already been processed. Exiting pipeline.")
        return

    # 🧵 Step 3: Run Parallel Execution Thread Pool
    logging.info(f"⚡ Starting multi-threaded pool with max_workers={max_workers}...")
    success_count = 0
    failure_count = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_policy = {executor.submit(process_single_policy, p): p for p in remaining_policies}
        
        for future in as_completed(future_to_policy):
            policy = future_to_policy[future]
            if future.result():
                success_count += 1
            else:
                failure_count += 1

    logging.info(f"🏁 Pipeline processing loop finished. Batch Success={success_count} | Batch Failures={failure_count}")

if __name__ == "__main__":
    # Adjust max_workers depending on your AWS Bedrock TPS limits (Defaulting to 5 concurrent worker threads)
    parallel_pipeline(max_workers=5)
