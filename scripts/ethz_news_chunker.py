import os
import json
import glob
import uuid
from typing import List, Dict, Any, Tuple
import numpy as np
from tqdm import tqdm
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Define paths
base_dir = '/content/news-qa-ethz1'
output_dir = '/content/news-qa-ethz1/'
chroma_db_path = os.path.join(output_dir, 'chroma_db')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize the embedding model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')  # Good for multiple languages

# Create a Chroma client
chroma_client = chromadb.PersistentClient(path=chroma_db_path)

# Create a collection
collection = chroma_client.get_or_create_collection(
    name="ethz_news",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
)

def fixed_size_chunking(text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:
    """Split text into fixed-size chunks with overlap."""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk:  # Ensure we don't add empty chunks
            chunks.append(chunk)
    
    return chunks

def semantic_segmentation(text: str, min_chunk_size: int = 100, similarity_threshold: float = 0.7) -> List[str]:
    """Split text into semantic chunks based on embedding similarity."""
    # First split into paragraphs
    paragraphs = [p for p in re.split(r'\n\n+', text) if p.strip()]
    
    if not paragraphs:
        return []
    
    # If only one paragraph or very short text, return as is
    if len(paragraphs) == 1 or len(text.split()) < min_chunk_size:
        return paragraphs
    
    # Calculate embeddings for each paragraph
    embeddings = model.encode(paragraphs)
    
    # Initialize chunks with the first paragraph
    chunks = [paragraphs[0]]
    current_chunk_embeddings = [embeddings[0]]
    
    # Iterate through paragraphs and merge similar ones
    for i in range(1, len(paragraphs)):
        current_paragraph = paragraphs[i]
        current_embedding = embeddings[i]
        
        # Calculate the average embedding of the current chunk
        avg_chunk_embedding = np.mean(current_chunk_embeddings, axis=0)
        
        # Calculate similarity between current paragraph and current chunk
        similarity = cosine_similarity([current_embedding], [avg_chunk_embedding])[0][0]
        
        # If similarity is high, merge with current chunk
        if similarity > similarity_threshold:
            chunks[-1] = chunks[-1] + "\n\n" + current_paragraph
            current_chunk_embeddings.append(current_embedding)
        else:
            # Start a new chunk
            chunks.append(current_paragraph)
            current_chunk_embeddings = [current_embedding]
    
    return chunks

def process_json_file(file_path: str) -> None:
    """Process a single JSON file, extract content, create chunks, and save to Chroma DB."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract main content text
        main_content = data.get('main_content', '')
        if not main_content:
            print(f"Warning: No main_content in {file_path}")
            return
        
        # Get metadata
        metadata = {
            "title": data.get('title', ''),
            "date": data.get('date', ''),
            "source": data.get('source', ''),
            "language": data.get('language', ''),
            "original_file": file_path,
            "named_entities": ", ".join(data.get('named_entities', [])),
            "topics": ", ".join(data.get('topics', [])),
            "keywords": ", ".join(data.get('keywords', [])),
            "summary": data.get('summary', '')
        }
        
        # Create chunks using both methods
        fixed_chunks = fixed_size_chunking(main_content)
        semantic_chunks = semantic_segmentation(main_content)
        
        all_chunks = []
        
        # Process fixed chunks
        for i, chunk in enumerate(fixed_chunks):
            chunk_id = f"fixed_{os.path.basename(file_path)}_{i}"
            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_method"] = "fixed_size"
            chunk_metadata["chunk_index"] = i
            
            all_chunks.append({
                "id": chunk_id,
                "text": chunk,
                "metadata": chunk_metadata
            })
        
        # Process semantic chunks
        for i, chunk in enumerate(semantic_chunks):
            chunk_id = f"semantic_{os.path.basename(file_path)}_{i}"
            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_method"] = "semantic"
            chunk_metadata["chunk_index"] = i
            
            all_chunks.append({
                "id": chunk_id,
                "text": chunk,
                "metadata": chunk_metadata
            })
        
        # Add chunks to Chroma DB
        for chunk in all_chunks:
            collection.add(
                documents=[chunk["text"]],
                metadatas=[chunk["metadata"]],
                ids=[chunk["id"]]
            )
        
        print(f"Processed {file_path}, added {len(all_chunks)} chunks to Chroma DB")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def find_json_files() -> List[str]:
    """Find all JSON files in the directory structure."""
    language_folders = ['de_internal', 'de_news_events', 'en_internal', 'en_news_events']
    json_files = []
    
    hk_news_path = os.path.join(base_dir, 'HKNews')
    
    for lang_folder in language_folders:
        lang_path = os.path.join(hk_news_path, lang_folder)
        
        if not os.path.exists(lang_path):
            print(f"Warning: Path does not exist - {lang_path}")
            continue
            
        # Handle the special case for 2017/01
        special_path = os.path.join(lang_path, '2017', '01')
        if os.path.exists(special_path):
            json_files.extend(glob.glob(os.path.join(special_path, '*.json')))
            
        # Handle regular year folders
        for year_dir in glob.glob(os.path.join(lang_path, '20*')):
            if os.path.isdir(year_dir):
                # Check if it's a year directory (not 2017/01)
                if os.path.basename(year_dir) != '2017' or not os.path.exists(os.path.join(year_dir, '01')):
                    for month_dir in glob.glob(os.path.join(year_dir, '*')):
                        if os.path.isdir(month_dir):
                            json_files.extend(glob.glob(os.path.join(month_dir, '*.json')))
    
    return json_files

def main():
    """Main function to process all JSON files."""
    json_files = find_json_files()
    
    print(f"Found {len(json_files)} JSON files to process")
    
    # Process each JSON file
    for file_path in tqdm(json_files, desc="Processing JSON files"):
        process_json_file(file_path)
    
    # Print some stats about the collection
    print(f"Total documents in Chroma DB: {collection.count()}")
    
    # Query example
    print("\nQuery example:")
    results = collection.query(
        query_texts=["brain research"],
        n_results=2
    )
    
    print(f"Query results: {results}")
    
    print("\nProcessing complete!")

if __name__ == "__main__":
    main()
