# Multilingual BM25 Retriever

A cross-lingual BM25 retrieval system for English and German documents, designed for easy integration with RAG systems.

## Features

🌍 **Cross-lingual search**: Search English documents with German queries and vice versa  
🔍 **Automatic language detection**: Detects query language automatically  
🔄 **Query translation**: Uses Google Translate for cross-lingual search  
⚡ **Enhanced BM25 scoring**: Optimized parameters and field weighting  
📁 **HKNews compatible**: Works directly with existing HKNews JSON structure  
🤖 **RAG ready**: Easy integration with RAG systems

## Quick Start

### Installation
```bash
pip install -e .
```

### Basic Usage
```python
from multilingual_bm25 import MultilingualBM25Retriever, load_hknews_documents, create_temp_documents
import shutil

# Load documents
documents = load_hknews_documents("HKNews/")
temp_dir = create_temp_documents(documents)

# Initialize retriever
retriever = MultilingualBM25Retriever(temp_dir)

# Search
results = retriever.search("artificial intelligence research", top_k=5)

# Display results
for result in results:
    print(f"[{result['language']}] {result['title']} (Score: {result['score']:.3f})")

# Clean up
shutil.rmtree(temp_dir)
```

### Interactive Demo
```bash
python scripts/simple_run.py
```

## Document Structure

The system expects JSON documents with this structure:

```json
{
  "id": "doc_001",
  "language": "en",
  "title": "Document Title",
  "main_content": "Full document content...",
  "summary": "Brief summary",
  "keywords": ["keyword1", "keyword2"],
  "topics": ["topic1", "topic2"]
}
```

## HKNews Directory Structure

Works with the following directory structure:

```
HKNews/
├── en_documents/
│   ├── 2023/
│   │   ├── 01/
│   │   │   ├── doc1.json
│   │   │   └── doc2.json
│   │   └── 02/
│   └── 2024/
└── de_documents/
    └── ...
```

## RAG Integration

For RAG systems:

```python
class MyRAGSystem:
    def __init__(self):
        documents = load_hknews_documents("HKNews/")
        self.temp_dir = create_temp_documents(documents)
        self.retriever = MultilingualBM25Retriever(self.temp_dir)
    
    def retrieve_context(self, query, top_k=3):
        results = self.retriever.search(query, top_k=top_k)
        
        context = []
        for result in results:
            context.append({
                'text': result['document']['main_content'],
                'title': result['title'],
                'score': result['score']
            })
        
        return context
    
    def cleanup(self):
        shutil.rmtree(self.temp_dir)
```

## API Reference

### MultilingualBM25Retriever

```python
retriever = MultilingualBM25Retriever(docs_directory)
```

- `docs_directory`: Path to directory containing JSON documents

#### Methods

**`search(query, top_k=5)`**
- Search for documents matching the query
- Returns: List of result dictionaries with scores and metadata

**`detect_language(query)`**  
- Detect the language of a query
- Returns: Language code ('en' or 'de')

### Data Loading

**`load_hknews_documents(source_dir="HKNews/")`**
- Load documents from HKNews directory structure
- Returns: List of processed documents

**`create_temp_documents(documents)`**
- Create temporary JSON files for the retriever
- Returns: Path to temporary directory

### Utilities

**`save_results(query, results, output_dir="bm25_query_results")`**
- Save search results to JSON file

**`run_interactive_search(retriever)`**
- Run interactive search session

## Examples

### Cross-lingual Search
```python
# English query finding German documents
results = retriever.search("machine learning", top_k=3)

# German query finding English documents  
results = retriever.search("maschinelles Lernen", top_k=3)
```


## Requirements
- numpy
- nltk  
- langdetect
- deep-translator
- rank-bm25

## Performance

- Automatic NLTK data download on first use
- Requires internet connection for translation
- Memory usage scales with corpus size
- Optimized BM25 parameters for small corpora

## File Structure

```
multilingual_bm25/
├── __init__.py          # Package exports
├── retriever.py         # Core MultilingualBM25Retriever class
├── data_loader.py       # HKNews document loading
├── utils.py             # Utility functions
└── README.md           # This file
```


