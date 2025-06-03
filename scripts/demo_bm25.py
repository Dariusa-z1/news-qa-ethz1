#!/usr/bin/env python3
"""
Simple runner for the Multilingual BM25 Retriever.
Just loads HKNews documents and runs interactive search.
"""

import sys
import shutil
from pathlib import Path

# Add the parent directory to the path so we can import our package
sys.path.insert(0, str(Path(__file__).parent.parent))

from multilingual_bm25 import (
    MultilingualBM25Retriever,
    load_hknews_documents,
    create_temp_documents,
    run_interactive_search
)


def main():
    """Load documents and run interactive search."""
    print("=== Multilingual BM25 Retriever ===")
    
    # Load documents from HKNews structure
    hknews_dir = "HKNews/"
    print(f"Loading documents from: {hknews_dir}")
    
    documents = load_hknews_documents(hknews_dir)
    
    if not documents:
        print("No documents found. Please check the HKNews directory path.")
        return 1
    
    # Create temporary directory for the retriever
    temp_dir = create_temp_documents(documents)
    
    try:
        # Initialize retriever
        print("Initializing retriever...")
        retriever = MultilingualBM25Retriever(temp_dir)
        
        # Run interactive search
        run_interactive_search(retriever)
        
    finally:
        # Clean up temporary files
        shutil.rmtree(temp_dir)
        print("Temporary files cleaned up")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())