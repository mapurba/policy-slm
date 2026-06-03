import json
import os

# 📁 Path Configurations - Updated to your specific folder
DATA_DIR = "/Users/ayoshi/Documents/source/policy-slm/training_data"

FILES_TO_CONVERT = {
    os.path.join(DATA_DIR, "train_split.jsonl"): os.path.join(DATA_DIR, "bedrock_train.jsonl"),
    os.path.join(DATA_DIR, "val.jsonl"): os.path.join(DATA_DIR, "bedrock_val.jsonl")
}

# 🧠 Define the System Persona for Bedrock
SYSTEM_PROMPT = "You are an expert AI assistant specializing in NetIQ Identity Manager DirXML policies, DTD rules, and enterprise identity engineering."

def convert_to_bedrock_format():
    print(f"📂 Looking for files in: {DATA_DIR}")
    for input_path, output_path in FILES_TO_CONVERT.items():
        if not os.path.exists(input_path):
            print(f"⚠️ Skipping: {os.path.basename(input_path)} not found in directory.")
            continue
            
        print(f"🔄 Converting {os.path.basename(input_path)}...")
        bedrock_lines = []
        
        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                
                # Combine instruction and input into a single clean user prompt
                user_text = f"{data['instruction']}\n\n[Context/Input]:\n{data['input']}" if data.get('input') else data['instruction']
                assistant_text = data['output']
                
                # Construct the bedrock-conversation-2024 structure
                bedrock_record = {
                    "schemaVersion": "bedrock-conversation-2024",
                    "system": [{"text": SYSTEM_PROMPT}],
                    "messages": [
                        {
                            "role": "user",
                            "content": [{"text": user_text}]
                        },
                        {
                            "role": "assistant",
                            "content": [{"text": assistant_text}]
                        }
                    ]
                }
                bedrock_lines.append(json.dumps(bedrock_record, ensure_ascii=False) + "\n")
        
        # Save the transformed dataset
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(bedrock_lines)
            
        print(f"✅ Saved Bedrock-compliant data to: {output_path}")

if __name__ == "__main__":
    convert_to_bedrock_format()