
import os
import sys
import argparse
from chromadb_utils import reassemble_chromadb

def main():
    parser = argparse.ArgumentParser(description='Load ChromaDB from GitHub parts')
    parser.add_argument('--repo-path', type=str, default='/content/news-qa-ethz1',
                        help='Path to the repository')
    parser.add_argument('--output-path', type=str, default='/content/news-qa-ethz1/chroma_db',
                        help='Path where to create the reassembled ChromaDB')
    
    args = parser.parse_args()
    
    print("ChromaDB Loader")
    print("==============")
    
    # Check if parts directory exists
    parts_dir = os.path.join(args.repo_path, "chromadb_parts")
    if not os.path.exists(parts_dir):
        print(f"Error: ChromaDB parts directory not found at {parts_dir}")
        return 1
    
    # Reassemble ChromaDB
    print(f"Reassembling ChromaDB at {args.output_path}...")
    try:
        reassemble_chromadb(args.repo_path, args.output_path)
        
        print("\nConnection example:")
        print("------------------")
        print("""
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path='{output_path}')
collection = client.get_collection(
    name="ethz_news",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
)
print(f"Connected to collection: {{collection.name}}")
print(f"Total documents in collection: {{collection.count()}}")
""".format(output_path=args.output_path))
        
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
