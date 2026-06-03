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
OUTPUT_FOLDER = "../policies"
MAX_FILENAME_LENGTH = 64
MAX_WORKERS = 20  # Adjust based on your network bandwidth and server courtesy

# Threading lock to prevent race conditions during file generation checks
file_system_lock = threading.Lock()

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

def save_rule_safely(directory, ideal_filename, rule_element):
    """
    Uses a thread lock to safely ensure unique filenames and write the file.
    Returns the final short filename used.
    """
    base_name, ext = os.path.splitext(ideal_filename)
    
    with file_system_lock:
        filepath = os.path.join(directory, ideal_filename)
        counter = 1
        
        # Resolve collisions if multiple threads match the same description
        while os.path.exists(filepath):
            suffix = f"_{counter}"
            max_base_len = MAX_FILENAME_LENGTH - len(ext) - len(suffix)
            truncated_base = base_name[:max_base_len]
            
            new_filename = f"{truncated_base}{suffix}{ext}"
            filepath = os.path.join(directory, new_filename)
            counter += 1
            
        # Write the file immediately while holding the lock to claim the path
        rule_xml_str = ET.tostring(rule_element, encoding='unicode', method='xml')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(rule_xml_str)
            
        return os.path.basename(filepath)

def process_single_jar(jar_url):
    """Worker function: Downloads and processes a single JAR file."""
    local_policies = []
    # Using a fresh requests session wrapper can be done, or standard get
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
                        # Thread-safe file writing
                        final_filename = save_rule_safely(OUTPUT_FOLDER, ideal_filename, rule)
                        
                        # Store the metadata temporarily (Main thread will assign sequential IDs)
                        local_policies.append(final_filename)
    except (zipfile.BadZipFile, ET.ParseError) as e:
        print(f"Error parsing archive content for {os.path.basename(jar_url)}: {e}")
        
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
        # Submit all tasks to the pool
        future_to_url = {executor.submit(process_single_jar, url): url for url in all_jar_urls}
        
        completed_count = 0
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                filenames = future.result()
                if filenames:
                    all_extracted_filenames.extend(filenames)
            except Exception as exc:
                print(f"{url} generated an explicit exception: {exc}")
            
            completed_count += 1
            if completed_count % 50 == 0 or completed_count == total_jars:
                print(f"Progress: {completed_count}/{total_jars} JARs evaluated...")

    # 3. Consolidate into index.json sequentially on the main thread
    print("Compiling global tracking index...")
    policies_index = []
    
    # Padding changed to :05d to support > 3000 rules safely without formatting breakage
    for index, filename in enumerate(all_extracted_filenames, start=1):
        policies_index.append({
            "id": f"policy-{index:05d}",
            "filename": filename
        })
        
    index_filepath = os.path.join(OUTPUT_FOLDER, 'index.json')
    with open(index_filepath, 'w', encoding='utf-8') as f:
        json.dump({"policies": policies_index}, f, indent=2)
        
    print(f"\nExecution Complete.")
    print(f"Total rules written: {len(policies_index)}")
    print(f"Output Catalog: {index_filepath}")

if __name__ == "__main__":
    main()