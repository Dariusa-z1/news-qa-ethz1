
import os
import shutil
import json
import subprocess
import glob
from datetime import datetime

def split_chromadb(chroma_db_path, output_parts_dir, max_part_size_mb=25):
    """
    Split a ChromaDB database into smaller parts for GitHub storage.
    
    Args:
        chroma_db_path: Path to the ChromaDB directory
        output_parts_dir: Directory to store the parts
        max_part_size_mb: Maximum size of each part in MB
        
    Returns:
        dict: Metadata about the split database
    """
    # Create output directory
    os.makedirs(output_parts_dir, exist_ok=True)
    
    # Get the collection ID (assuming there's just one collection folder in ChromaDB)
    collection_dirs = [d for d in os.listdir(chroma_db_path) 
                      if os.path.isdir(os.path.join(chroma_db_path, d)) 
                      and len(d) == 36]  # UUID is 36 chars
    
    if not collection_dirs:
        raise ValueError(f"No collection directory found in {chroma_db_path}")
    
    collection_id = collection_dirs[0]
    print(f"Found collection ID: {collection_id}")
    
    # Track all files we need to split
    files_to_split = []
    
    # Add the SQLite database
    sqlite_path = os.path.join(chroma_db_path, "chroma.sqlite3")
    if os.path.exists(sqlite_path):
        files_to_split.append(("sqlite3", sqlite_path))
    
    # Add any large binary files in the collection directory
    collection_dir = os.path.join(chroma_db_path, collection_id)
    for file_path in glob.glob(os.path.join(collection_dir, "*.bin")):
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > max_part_size_mb:
            file_name = os.path.basename(file_path)
            files_to_split.append((file_name, file_path))
    
    # Create metadata about the database
    metadata = {
        "collection_id": collection_id,
        "max_part_size_mb": max_part_size_mb,
        "files": []
    }
    
    # Split large files
    for file_id, file_path in files_to_split:
        file_name = os.path.basename(file_path)
        print(f"Splitting {file_name}...")
        
        # Create parts with split command
        prefix = os.path.join(output_parts_dir, f"{file_id}_part_")
        cmd = f"split -b {max_part_size_mb}M {file_path} {prefix}"
        subprocess.run(cmd, shell=True, check=True)
        
        # Get list of generated parts
        parts = sorted(glob.glob(f"{prefix}*"))
        
        # Add to metadata
        metadata["files"].append({
            "id": file_id,
            "original_path": os.path.relpath(file_path, chroma_db_path),
            "parts": [os.path.basename(p) for p in parts]
        })
    
    # Copy smaller files directly
    small_files = []
    for ext in ["*.bin", "*.pickle"]:
        for file_path in glob.glob(os.path.join(collection_dir, ext)):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_mb <= max_part_size_mb:
                file_name = os.path.basename(file_path)
                print(f"Copying small file: {file_name}")
                dest_path = os.path.join(output_parts_dir, file_name)
                shutil.copy2(file_path, dest_path)
                small_files.append({
                    "original_path": os.path.relpath(file_path, chroma_db_path),
                    "part": file_name
                })
    
    metadata["small_files"] = small_files
    
    # Save metadata
    manifest_path = os.path.join(output_parts_dir, "manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Database split complete. Parts and manifest saved to {output_parts_dir}")
    return metadata

def reassemble_chromadb(repo_path, output_db_path):
    """
    Reassemble a ChromaDB database from parts stored in a GitHub repository.
    
    Args:
        repo_path: Path to the repository root
        output_db_path: Path where to create the reassembled ChromaDB
    """
    parts_dir = os.path.join(repo_path, "chromadb_parts")
    manifest_path = os.path.join(parts_dir, "manifest.json")
    
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest file not found at {manifest_path}")
    
    # Load the manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    # Create output directory
    os.makedirs(output_db_path, exist_ok=True)
    
    # Create collection directory
    collection_id = manifest["collection_id"]
    collection_dir = os.path.join(output_db_path, collection_id)
    os.makedirs(collection_dir, exist_ok=True)
    
    # Reassemble split files
    for file_info in manifest["files"]:
        file_id = file_info["id"]
        original_path = file_info["original_path"]
        output_file = os.path.join(output_db_path, original_path)
        
        # Make sure the directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        print(f"Reassembling {original_path}...")
        
        # Create an empty target file
        open(output_file, 'wb').close()
        
        # Concatenate all parts
        for part_name in file_info["parts"]:
            part_path = os.path.join(parts_dir, part_name)
            with open(part_path, 'rb') as part_file:
                with open(output_file, 'ab') as target_file:
                    shutil.copyfileobj(part_file, target_file)
    
    # Copy all small files
    for file_info in manifest["small_files"]:
        original_path = file_info["original_path"]
        part_name = file_info["part"]
        
        source_path = os.path.join(parts_dir, part_name)
        dest_path = os.path.join(output_db_path, original_path)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        print(f"Copying {original_path}")
        shutil.copy2(source_path, dest_path)
    
    print(f"ChromaDB reassembly complete at {output_db_path}")
