
import os
import shutil
import subprocess

# Define paths
chroma_db_path = 'chroma_db'
parts_dir = 'chromadb_parts'

# Read the structure file to understand the original directory layout
with open(os.path.join(parts_dir, 'structure.txt'), 'r') as f:
    structure = f.read().splitlines()

# Extract the collection UUID from the structure
collection_uuid = None
for line in structure:
    if '/chroma_db/' in line and len(line.split('/')[-2]) == 36:
        collection_uuid = line.split('/')[-2]
        break

if not collection_uuid:
    print("Could not determine collection UUID from structure file")
    exit(1)

# Create the necessary directories
os.makedirs(chroma_db_path, exist_ok=True)
collection_path = os.path.join(chroma_db_path, collection_uuid)
os.makedirs(collection_path, exist_ok=True)

# Combine the split SQLite database
print("Reconstructing SQLite database...")
with open(os.path.join(chroma_db_path, 'chroma.sqlite3'), 'wb') as outfile:
    sqlite_parts = sorted([f for f in os.listdir(parts_dir) if f.startswith('sqlite3_part_')])
    for part in sqlite_parts:
        with open(os.path.join(parts_dir, part), 'rb') as infile:
            outfile.write(infile.read())

# Combine the split data_level0.bin file
print("Reconstructing data_level0.bin...")
with open(os.path.join(collection_path, 'data_level0.bin'), 'wb') as outfile:
    level0_parts = sorted([f for f in os.listdir(parts_dir) if f.startswith('data_level0_part_')])
    for part in level0_parts:
        with open(os.path.join(parts_dir, part), 'rb') as infile:
            outfile.write(infile.read())

# Copy the smaller files
for file in ['header.bin', 'index_metadata.pickle', 'length.bin', 'link_lists.bin']:
    if os.path.exists(os.path.join(parts_dir, file)):
        shutil.copy(os.path.join(parts_dir, file), os.path.join(collection_path, file))
        print(f"Copied {file}")

print("\nChromaDB reconstruction complete!")
