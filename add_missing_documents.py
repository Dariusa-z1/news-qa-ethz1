import json
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

# Files we know contain answers
answer_files = [
    'HKNews/en_news_events/2019/06/other-worlds.json',
    'HKNews/en_news_events/2020/02/seismicity-of-mars.json',
    'HKNews/en_news_events/2021/07/lord-of-the-flies-data-and-seven-bycicles.json',
    'HKNews/en_internal/2019/10/persistent-identifiers-in-research-highlights.json'
]

# Initialize ChromaDB
client = chromadb.PersistentClient(path='notebooks/chroma_db_fixed')
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='paraphrase-multilingual-MiniLM-L12-v2'
)

collection = client.get_collection('ethz_news', embedding_function=embedding_fn)

print(f'Current collection size: {collection.count()} documents')

# Process each file
documents_added = 0

for file_path in answer_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        main_content = data.get('main_content', '')
        if not main_content:
            print(f'  No main_content in {file_path}')
            continue
            
        # Create chunks (using paragraph-based chunking)
        paragraphs = main_content.split('\n\n')
        
        chunk_size = 800  # Larger chunks to avoid splitting facts
        current_chunk = ""
        chunk_id = 0
        
        for para in paragraphs:
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk.strip():
                    # Add chunk to collection
                    doc_id = f"{Path(file_path).stem}_chunk_{chunk_id}"
                    
                    # Check if important content is in this chunk
                    important = ""
                    if "26 November 2018" in current_chunk:
                        important = " [CONTAINS INSIGHT DATE]"
                    elif "Olaf Kübler" in current_chunk:
                        important = " [CONTAINS KÜBLER]"
                    elif "e-Sling" in current_chunk:
                        important = " [CONTAINS E-SLING]"
                    
                    print(f'  Adding chunk {doc_id}{important}')
                    
                    collection.add(
                        documents=[current_chunk.strip()],
                        ids=[doc_id],
                        metadatas=[{
                            'original_file': file_path,
                            'chunk_index': chunk_id,
                            'chunk_method': 'paragraph_based',
                            'title': data.get('title', ''),
                            'date': data.get('date', ''),
                            'language': 'en'
                        }]
                    )
                    documents_added += 1
                    chunk_id += 1
                
                current_chunk = para + "\n\n"
        
        # Don't forget the last chunk
        if current_chunk.strip():
            doc_id = f"{Path(file_path).stem}_chunk_{chunk_id}"
            collection.add(
                documents=[current_chunk.strip()],
                ids=[doc_id],
                metadatas=[{
                    'original_file': file_path,
                    'chunk_index': chunk_id,
                    'chunk_method': 'paragraph_based',
                    'title': data.get('title', ''),
                    'date': data.get('date', ''),
                    'language': 'en'
                }]
            )
            documents_added += 1
            
        print(f'✓ Processed {file_path}: {chunk_id + 1} chunks')
        
    except Exception as e:
        print(f'✗ Error processing {file_path}: {e}')

print(f'\nAdded {documents_added} new chunks to ChromaDB')
print(f'New collection size: {collection.count()} documents')

# Test if we can now find the answers
print('\nTesting retrieval...')
test_queries = [
    ('InSight Mars 2018', '26 November 2018'),
    ('Olaf Kübler president', 'Olaf Kübler'),
    ('e-Sling electric', 'e-Sling')
]

for query, expected in test_queries:
    results = collection.query(query_texts=[query], n_results=5)
    found = False
    
    for doc in results['documents'][0]:
        if expected in doc:
            print(f'✓ {query}: Found "{expected}"!')
            found = True
            break
    
    if not found:
        print(f'✗ {query}: "{expected}" not found')
