"""
Dense/ChromaDB Adapter for Hybrid Retrieval System
Wraps ChromaDB vector search to provide a unified interface
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict, Any, Tuple
import json


class DenseAdapter:
    """Adapter for ChromaDB dense retrieval to work with hybrid system"""
    
    def __init__(self, chroma_db_path: str = "chroma_db", 
                 collection_name: str = "ethz_news",
                 model_name: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        """
        Initialize Dense/ChromaDB adapter
        
        Args:
            chroma_db_path: Path to ChromaDB database
            collection_name: Name of the collection to use
            model_name: Name of the sentence transformer model
        """
        # Check if ChromaDB needs to be reassembled
        if not os.path.exists(chroma_db_path) and os.path.exists("chromadb_parts"):
            print("ChromaDB not found, attempting to reassemble from parts...")
            from scripts.chromadb_utils import reassemble_chromadb
            reassemble_chromadb(".", chroma_db_path)
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(path=chroma_db_path)
        
        # Get or create collection with embedding function
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=model_name
        )
        
        try:
            self.collection = self.client.get_collection(
                name=collection_name,
                embedding_function=self.embedding_function
            )
        except:
            # Collection doesn't exist, create it
            self.collection = self.client.create_collection(
                name=collection_name,
                embedding_function=self.embedding_function
            )
        
        self.name = "Dense_ChromaDB"
        print(f"ChromaDB initialized with {self.collection.count()} documents")
    
    def retrieve(self, query: str, top_k: int = 10) -> List[Tuple[Dict[str, Any], float]]:
        """
        Retrieve documents using dense/vector search
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of tuples (document_dict, score)
        """
        # Query the collection
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
            include=['documents', 'metadatas', 'distances']
        )
        
        # Standardize the output format
        standardized_results = []
        
        # ChromaDB returns lists of lists, we need the first list
        documents = results['documents'][0] if results['documents'] else []
        metadatas = results['metadatas'][0] if results['metadatas'] else []
        distances = results['distances'][0] if results['distances'] else []
        
        for idx, (doc, metadata, distance) in enumerate(zip(documents, metadatas, distances)):
            # Convert distance to similarity score (inverse of distance)
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