import os
import re
import json
import requests
import zipfile
import io
import threading
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Configuration Variables ---
TARGET_URLS = [
    "https://nu.novell.com/designer/packages/ilm/updatesite_1_0_0/plugins/",
    "https://nu.novell.com/designer/packages/idm/updatesite2_0_0/plugins/",
    "https://nu.novell.com/designer/packages/idm/updatesite1_0_0/plugins/"
]
OUTPUT_FOLDER = "../policies_unique"
MAX_FILENAME_LENGTH = 64
MAX_WORKERS = 20

# Threading lock and global set to track uniqueness
file_system_lock = threading.Lock()
seen_rule_names = set()

def sanitize_filename(description):
    """Sanitizes the description to create a safe, limited-length filename."""
    if not description:
        description = "unnamed_rule"
        
    clean_name = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', description).strip()
    
    ext = ".xml"
    max_base_len = MAX_FILENAME_LENGTH - len(ext)
    
    base_name = clean_name[:max_base_len].strip('_')
    if not base_name:
        base_name = "rule"
        
    return f"{base_name}{ext}"

def save_rule_if_unique(directory, ideal_filename, rule_element):
    """
    Uses a thread lock to check if we've seen this rule name before.
    If it's new, saves it. If it's a duplicate, skips it.
    Returns the filename if saved, or None if skipped.
    """
    with file_system_lock:
        # Check if we already extracted a version of this policy
        if ideal_filename in seen_rule_names:
            return None 
            
        # If it's unique, add it to the tracking set
        seen_rule_names.add(ideal_filename)
        
        filepath = os.path.join(directory, ideal_filename)
        
        # Write the file immediately while holding the lock
        rule_xml_str = ET.tostring(rule_element, encoding='unicode', method='xml')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(rule_xml_str)
            
        return ideal_filename

def process_single_jar(jar_url):
    """Worker function: Downloads and processes a single JAR file."""
    local_policies = []
    
    try:
        response = requests.get(jar_url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error downloading {jar_url}: {e}")
        return local_policies

    try:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            if 'package_import.xml' in z.namelist():
                xml_content = z.read('package_import.xml')
                root = ET.fromstring(xml_content)
                
                for rule in root.findall('.//rule'):
                    conditions = rule.find('conditions')
                    actions = rule.find('actions')
                    
                    if conditions is not None and actions is not None:
                        desc_elem = rule.find('description')
                        desc_text = desc_elem.text if desc_elem is not None and desc_elem.text else "missing_description"
                        
                        ideal_filename = sanitize_filename(desc_text)
                        
                        # Only returns a filename if it hasn't been saved by another thread yet
                        saved_filename = save_rule_if_unique(OUTPUT_FOLDER, ideal_filename, rule)
                        
                        if saved_filename:
                            local_policies.append(saved_filename)
                            
    except (zipfile.BadZipFile, ET.ParseError) as e:
        pass # Silently skip unreadable archives to keep the console clean
        
    return local_policies

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # 1. Gather and deduplicate all JAR URLs upfront
    all_jar_urls = set()
    print("Gathering targets and deduplicating archive paths...")
    
    for base_url in TARGET_URLS:
        try:
            res = requests.get(base_url, timeout=15)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if href.endswith('.jar'):
                    all_jar_urls.add(urljoin(base_url, href))
        except requests.RequestException as e:
            print(f"Skipping index URL {base_url} due to error: {e}")

    total_jars = len(all_jar_urls)
    print(f"Found {total_jars} unique JAR files to process.")

    # 2. Process JARs in parallel
    all_extracted_filenames = []
    
    print(f"Starting parallel execution pool with {MAX_WORKERS} workers...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(process_single_jar, url): url for url in all_jar_urls}
        
        completed_count = 0
        for future in as_completed(future_to_url):
            try:
                filenames = future.result()
                if filenames:
                    all_extracted_filenames.extend(filenames)
            except Exception:
                pass 
            
            completed_count += 1
            if completed_count % 50 == 0 or completed_count == total_jars:
                print(f"Progress: {completed_count}/{total_jars} JARs evaluated...")

    # 3. Consolidate into index.json sequentially on the main thread
    print("\nCompiling global tracking index...")
    policies_index = []
    
    # Sort filenames alphabetically so the JSON index is clean and predictable
    all_extracted_filenames.sort()
    
    for index, filename in enumerate(all_extracted_filenames, start=1):
        policies_index.append({
            "id": f"policy-{index:05d}",
            "filename": filename
        })
        
    index_filepath = os.path.join(OUTPUT_FOLDER, 'index.json')
    with open(index_filepath, 'w', encoding='utf-8') as f:
        json.dump({"policies": policies_index}, f, indent=2)
        
    print(f"Execution Complete.")
    print(f"Total UNIQUE rules written: {len(policies_index)}")
    print(f"Output Catalog: {index_filepath}")

if __name__ == "__main__":
    main()