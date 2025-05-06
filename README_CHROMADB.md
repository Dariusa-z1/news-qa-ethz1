# ETH News ChromaDB

This repository contains scripts to process ETH Zürich news articles and query them using ChromaDB.

## Setup

The ChromaDB is split into parts to accommodate GitHub's file size limits. To set up:

1. Clone this repository
2. Run `python scripts/reassemble_chromadb.py` to rebuild the database from parts
3. Use the database as shown below

## Usage

```python
import chromadb
from chromadb.utils import embedding_functions

# Connect to the database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(
    name="ethz_news",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
)

# Run a semantic search
results = collection.query(
    query_texts=["brain research"],
    n_results=5
)
