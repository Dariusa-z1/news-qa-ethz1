
import os
import glob
import shutil

def reassemble_chromadb(repo_path, output_path):
    """
    Reassemble ChromaDB from split parts stored in the repository.
    
    Args:
        repo_path: Path to the repository containing chromadb_parts
        output_path: Where to reassemble the complete database
    """
    parts_dir = os.path.join(repo_path, "chromadb_parts")
    
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    # Get the UUID directory name from manifest.json or create one
    manifest_path = os.path.join(parts_dir, "manifest.json")
    if os.path.exists(manifest_path):
        import json
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
            uuid_dir = manifest.get('uuid_directory', 'd9725886-aef5-45f7-af6b-dfffc099700c')
    else:
        # Default UUID if manifest doesn't exist
        uuid_dir = 'd9725886-aef5-45f7-af6b-dfffc099700c'
    
    collection_path = os.path.join(output_path, uuid_dir)
    os.makedirs(collection_path, exist_ok=True)
    
    print("Reassembling chroma.sqlite3...")
    # Reassemble the SQLite database
    sqlite_parts = sorted(glob.glob(os.path.join(parts_dir, "sqlite3_part_*")))
    if sqlite_parts:
        with open(os.path.join(output_path, "chroma.sqlite3"), "wb") as outfile:
            for part in sqlite_parts:
                print(f"  Adding {os.path.basename(part)}")
                with open(part, "rb") as infile:
                    outfile.write(infile.read())
    
    print("Reassembling data_level0.bin...")
    # Reassemble the data_level0.bin file
    data_parts = sorted(glob.glob(os.path.join(parts_dir, "data_level0.bin_part_*")))
    if data_parts:
        with open(os.path.join(collection_path, "data_level0.bin"), "wb") as outfile:
            for part in data_parts:
                print(f"  Adding {os.path.basename(part)}")
                with open(part, "rb") as infile:
                    outfile.write(infile.read())
    
    # Copy other files
    other_files = [
        "header.bin",
        "index_metadata.pickle",
        "length.bin",
        "link_lists.bin"
    ]
    
    for file in other_files:
        source_path = os.path.join(parts_dir, file)
        dest_path = os.path.join(collection_path, file)
        
        if os.path.exists(source_path):
            print(f"Copying {file}")
            shutil.copy2(source_path, dest_path)
        else:
            print(f"Warning: {file} not found in parts directory")
            # Try to find it in the original chroma_db if it exists
            original_db = os.path.join(repo_path, "chroma_db")
            if os.path.exists(original_db):
                # Find UUID directory in original
                uuid_dirs = [d for d in os.listdir(original_db) 
                            if os.path.isdir(os.path.join(original_db, d)) 
                            and len(d) == 36]
                if uuid_dirs:
                    original_file = os.path.join(original_db, uuid_dirs[0], file)
                    if os.path.exists(original_file):
                        print(f"  Found {file} in original database, copying...")
                        shutil.copy2(original_file, dest_path)
                    else:
                        print(f"  {file} not found in original database either")
    
    print("Database reassembly completed!")

def verify_chromadb(db_path):
    """
    Verify that the ChromaDB is properly assembled and functional.
    """
    # Check if main files exist
    sqlite_path = os.path.join(db_path, "chroma.sqlite3")
    if not os.path.exists(sqlite_path):
        return False, "chroma.sqlite3 not found"
    
    # Check for collection directory
    collection_dirs = [d for d in os.listdir(db_path) 
                      if os.path.isdir(os.path.join(db_path, d)) 
                      and len(d) == 36]
    
    if not collection_dirs:
        return False, "No collection directory found"
    
    collection_path = os.path.join(db_path, collection_dirs[0])
    required_files = ["data_level0.bin", "header.bin", "index_metadata.pickle", "length.bin", "link_lists.bin"]
    
    for file in required_files:
        if not os.path.exists(os.path.join(collection_path, file)):
            return False, f"{file} not found in collection directory"
    
    return True, "ChromaDB verification successful"
