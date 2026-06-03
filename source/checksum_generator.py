import os
import json
import hashlib

# --- Configuration ---
# Provide the path to your index.json here. 
# It can be a relative path (like below) or a full absolute path.
INDEX_FILE_PATH = "/Users/ayoshi/Documents/source/policy-slm/policies_unique/index.json"

def calculate_checksum(file_path):
    """
    Reads the file, strips leading and trailing whitespace, 
    and returns a SHA-256 checksum.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip any pre or trailing spaces/newlines
    cleaned_content = content.strip()
    
    # Generate the SHA-256 hash
    sha256_hash = hashlib.sha256(cleaned_content.encode('utf-8')).hexdigest()
    
    return sha256_hash

def main():
    if not os.path.exists(INDEX_FILE_PATH):
        print(f"Error: Could not find index file at '{INDEX_FILE_PATH}'.")
        return

    # Automatically determine the folder containing the XML files 
    # based on where the index.json is located.
    base_dir = os.path.dirname(INDEX_FILE_PATH)

    # 1. Load the existing index
    print(f"Reading index file: {INDEX_FILE_PATH}")
    with open(INDEX_FILE_PATH, 'r', encoding='utf-8') as f:
        try:
            index_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return

    policies = index_data.get("policies", [])
    if not policies:
        print("No policies found in the index file.")
        return

    print(f"Found {len(policies)} policies. Calculating checksums...")
    
    success_count = 0
    missing_count = 0

    # 2. Iterate through each policy
    for policy in policies:
        filename = policy.get("filename")
        if not filename:
            continue

        file_path = os.path.join(base_dir, filename)

        if os.path.exists(file_path):
            # Calculate and inject the checksum into the dictionary
            policy["checksum"] = calculate_checksum(file_path)
            success_count += 1
        else:
            print(f"  [WARNING] File missing on disk: {file_path}")
            missing_count += 1

    # 3. Write the updated data back to the index.json file
    print("Writing updated data back to the index file...")
    with open(INDEX_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2)

    print("\n--- Execution Complete ---")
    print(f"Successfully updated {success_count} policies with checksums.")
    if missing_count > 0:
        print(f"Skipped {missing_count} policies because the files were missing.")

if __name__ == "__main__":
    main()