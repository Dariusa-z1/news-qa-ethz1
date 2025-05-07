
# ChromaDB GitHub Storage Utilities

This directory contains utility scripts to manage ChromaDB with GitHub. The scripts handle splitting, 
reassembling, and loading ChromaDB databases that exceed GitHub's file size limits.

## Scripts Overview

- `chromadb_utils.py`: Core utility functions for splitting and reassembling ChromaDB
- `split_and_save_chromadb.py`: Script to split a ChromaDB database into smaller parts for GitHub storage
- `load_chromadb.py`: Script to reassemble a ChromaDB database from GitHub parts

## Usage

### For Repository Maintainers

1. **Split ChromaDB for GitHub storage**:

```bash
python scripts/split_and_save_chromadb.py --db-path /path/to/chroma_db --parts-dir /path/to/chromadb_parts
