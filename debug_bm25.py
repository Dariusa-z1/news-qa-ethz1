import os
import json

# Check HKNews structure
hknews_path = "HKNews"
total_files = 0

for root, dirs, files in os.walk(hknews_path):
    json_files = [f for f in files if f.endswith('.json')]
    if json_files:
        print(f"\nDirectory: {root}")
        print(f"JSON files found: {len(json_files)}")
        total_files += len(json_files)
        
        # Try to load one file as example
        if json_files:
            sample_file = os.path.join(root, json_files[0])
            try:
                with open(sample_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"Sample file structure: {list(data.keys())[:5]}...")
            except Exception as e:
                print(f"Error loading {sample_file}: {e}")

print(f"\nTotal JSON files found: {total_files}")