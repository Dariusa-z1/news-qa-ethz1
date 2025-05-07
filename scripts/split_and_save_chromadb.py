
import os
import sys
import argparse
from chromadb_utils import split_chromadb

def main():
    parser = argparse.ArgumentParser(description='Split ChromaDB for GitHub storage')
    parser.add_argument('--db-path', type=str, default='/content/news-qa-ethz1/chroma_db',
                        help='Path to the ChromaDB directory')
    parser.add_argument('--parts-dir', type=str, default='/content/news-qa-ethz1/chromadb_parts',
                        help='Directory to store the ChromaDB parts')
    parser.add_argument('--max-part-size', type=int, default=25,
                        help='Maximum size of each part in MB')
    
    args = parser.parse_args()
    
    print("ChromaDB Splitter")
    print("================")
    
    # Check if ChromaDB exists
    if not os.path.exists(args.db_path):
        print(f"Error: ChromaDB directory not found at {args.db_path}")
        return 1
    
    # Create parts directory if it doesn't exist
    os.makedirs(args.parts_dir, exist_ok=True)
    
    # Split ChromaDB
    print(f"Splitting ChromaDB into parts (max {args.max_part_size}MB each)...")
    try:
        metadata = split_chromadb(args.db_path, args.parts_dir, args.max_part_size)
        
        print("\nGit commands to update repository:")
        print("----------------------------------")
        print("# Add new ChromaDB parts")
        print(f"git add {os.path.dirname(args.parts_dir)}/chromadb_parts/")
        print(f"git add {os.path.dirname(args.parts_dir)}/scripts/")
        print("git commit -m 'Add updated ChromaDB parts'")
        print("git push origin main")  # Or your branch name
        
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
