import os
import random
import logging

# 📁 File Configurations (Using your absolute paths)
INPUT_FILE = "/Users/ayoshi/Documents/source/policy-slm/training_data/train.jsonl"
TRAIN_OUTPUT_FILE = "/Users/ayoshi/Documents/source/policy-slm/training_data/train_split.jsonl"
VAL_OUTPUT_FILE = "/Users/ayoshi/Documents/source/policy-slm/training_data/val.jsonl"
LOG_FILE = "/Users/ayoshi/Documents/source/policy-slm/pipeline.log"

# 📝 Configure Python Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def shuffle_and_split():
    logging.info("🚀 Starting dataset shuffle and split process...")

    if not os.path.exists(INPUT_FILE):
        logging.error(f"❌ Input file not found at: {INPUT_FILE}")
        return

    # 📖 1. Read all JSONL lines into memory
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    logging.info(f"📊 Loaded {total_lines} total training pairs from {INPUT_FILE}")

    if total_lines == 0:
        logging.warning("⚠️ No data found in the input file. Exiting.")
        return

    # 🔀 2. Shuffle the dataset
    logging.info("🔀 Randomly shuffling the dataset to distribute tasks evenly...")
    random.seed(42)  # Ensures the random shuffle is reproducible
    random.shuffle(lines)

    # ✂️ 3. Calculate the 90% split index
    split_index = int(total_lines * 0.9)
    train_lines = lines[:split_index]
    val_lines = lines[split_index:]

    logging.info(f"⚖️ Splitting complete: {len(train_lines)} for Training (90%), {len(val_lines)} for Validation (10%)")

    # 💾 4. Write the Training data
    logging.info(f"💾 Saving training split to {TRAIN_OUTPUT_FILE}...")
    with open(TRAIN_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(train_lines)

    # 💾 5. Write the Validation data
    logging.info(f"💾 Saving validation split to {VAL_OUTPUT_FILE}...")
    with open(VAL_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(val_lines)

    logging.info("✅ Dataset preparation successfully completed! Ready for fine-tuning.")

if __name__ == "__main__":
    shuffle_and_split()