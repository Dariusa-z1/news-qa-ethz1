"""
Fixed Dense/ChromaDB Adapter that uses the correct database
"""
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict, Any, Tuple
from pathlib import Path

class DenseAdapter:
    """Fixed adapter for ChromaDB dense retrieval"""
    
    def __init__(self):
        """Initialize with the correct ChromaDB path and collection"""
        # Use the fixed path
        chroma_db_path = Path(__file__).resolve().parent.parent.parent / "notebooks" / "chroma_db_fixed"
        
        print(f"📂 Loading ChromaDB from: {chroma_db_path}")
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(path=str(chroma_db_path))
        
        # Use the correct embedding function
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        
        # Get the ethz_news collection
        try:
            self.collection = self.client.get_collection(
                name="ethz_news",
                embedding_function=self.embedding_function
            )
            self.name = "Dense_ChromaDB"
            print(f"✅ ChromaDB initialized with {self.collection.count():,} documents from 'ethz_news'")
        except Exception as e:
            print(f"❌ Error loading collection: {e}")
            raise
    
    def retrieve(self, query: str, top_k: int = 10) -> List[Tuple[Dict[str, Any], float]]:
        """Retrieve documents using dense/vector search"""
        # Query the collection
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
            include=['documents', 'metadatas', 'distances']
        )
        
        # Standardize the output format
        standardized_results = []
        
        documents = results['documents'][0] if results['documents'] else []
        metadatas = results['metadatas'][0] if results['metadatas'] else []
        distances = results['distances'][0] if results['distances'] else []
        
        for idx, (doc, metadata, distance) in enumerate(zip(documents, metadatas, distances)):
            # Convert distance to similarity score
            score = 1.0 / (1.0 + distance)
            
            doc_dict = {
                'id': metadata.get('id', f"dense_{idx}"),
                'content': doc,
                'title': metadata.get('title', ''),
                'metadata': metadata,
                'retriever': self.name,
                'distance': distance
            }
            standardized_results.append((doc_dict, score))
        
        return standardized_results
    
    def get_name(self) -> str:
        """Return the name of this retriever"""
        return self.name
    
    def get_document_count(self) -> int:
        """Return the number of documents in the collection"""
        return self.collection.count()
