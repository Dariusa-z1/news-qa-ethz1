#!/usr/bin/env python
"""
Reassemble the ChromaDB database from parts.
"""
import os
import glob
import shutil

# Create directories
os.makedirs("chroma_db/d9725886-aef5-45f7-af6b-dfffc099700c", exist_ok=True)

# Reassemble the SQLite database
print("Reassembling chroma.sqlite3...")
with open("chroma_db/chroma.sqlite3", "wb") as outfile:
    parts = sorted(glob.glob("chromadb_parts/sqlite3_part_*"))
    for part in parts:
        print(f"  Adding {part}")
        with open(part, "rb") as infile:
            outfile.write(infile.read())

# Reassemble the data_level0.bin file
print("Reassembling data_level0.bin...")
with open("chroma_db/d9725886-aef5-45f7-af6b-dfffc099700c/data_level0.bin", "wb") as outfile:
    parts = sorted(glob.glob("chromadb_parts/data_level0_part_*"))
    for part in parts:
        print(f"  Adding {part}")
        with open(part, "rb") as infile:
            outfile.write(infile.read())

# Copy the other smaller files directly
small_files = [
    "header.bin",
    "index_metadata.pickle",
    "length.bin",
    "link_lists.bin"
]

for file in small_files:
    src = f"chromadb_parts/{file}"
    dst = f"chroma_db/d9725886-aef5-45f7-af6b-dfffc099700c/{file}"
    if os.path.exists(src):
        print(f"Copying {file}...")
        shutil.copy(src, dst)

print("Database reassembly complete!")
