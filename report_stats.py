from pathlib import Path

files = {
    "Policy training records": "train.jsonl",
    "DTD tag training records": "training_data/dtd_train.jsonl",
    "Merged training records": "training_data/train_merged.jsonl"
}

print("Training Dataset Statistics:")
print("=" * 50)
for label, path in files.items():
    p = Path(path)
    count = sum(1 for _ in p.open('r', encoding='utf-8')) if p.exists() else 0
    print(f"{label:.<40} {count:>8}")
