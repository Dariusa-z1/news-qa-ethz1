"""
BM25 Adapter for Hybrid Retrieval System
Wraps the existing Multilingual BM25 retriever to provide a unified interface
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from multilingual_bm25 import MultilingualBM25Retriever
from typing import List, Dict, Any, Tuple
import pickle


class BM25Adapter:
    """Adapter for BM25 retriever to work with hybrid system"""
    
    def __init__(self, docs_directory: str = "HKNews"):
        """
        Initialize BM25 adapter
        
        Args:
            docs_directory: Path to directory containing JSON documents
        """
        # The MultilingualBM25Retriever expects a directory path
        self.retriever = MultilingualBM25Retriever(docs_directory)
        self.name = "BM25"
    
    def retrieve(self, query: str, top_k: int = 10) -> List[Tuple[Dict[str, Any], float]]:
        """
        Retrieve documents using BM25
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of tuples (document_dict, score)
        """
        try:
            # Try different method names that might exist
            if hasattr(self.retriever, 'search'):
                results = self.retriever.search(query, top_k=top_k)
            elif hasattr(self.retriever, 'query'):
                results = self.retriever.query(query, top_k=top_k)
            elif hasattr(self.retriever, 'get_top_n'):
                results = self.retriever.get_top_n(query, n=top_k)
            elif hasattr(self.retriever, 'search_multilingual'):
                results = self.retriever.search_multilingual(query, top_k=top_k)
            else:
                # List all available methods for debugging
                methods = [method for method in dir(self.retriever) 
                          if not method.startswith('_') and callable(getattr(self.retriever, method))]
                print(f"Available methods in BM25 retriever: {methods}")
                return []
            
            # Standardize the output format
            standardized_results = []
            
            # Handle different possible result formats
            if isinstance(results, list):
                for idx, result in enumerate(results):
                    if isinstance(result, tuple) and len(result) == 2:
                        # Expected format: (doc_info, score)
                        doc_info, score = result
                    elif isinstance(result, dict):
                        # Result is a dictionary
                        doc_info = result
                        score = result.get('score', 1.0 / (idx + 1))
                    else:
                        # Unknown format
                        doc_info = {'content': str(result)}
                        score = 1.0 / (idx + 1)
                    
                    # Create standardized document
                    doc_dict = {
                        'id': doc_info.get('id', f"bm25_{idx}"),
                        'content': doc_info.get('content', doc_info.get('text', '')),
                        'title': doc_info.get('title', ''),
                        'metadata': {
                            'language': doc_info.get('language', 'unknown'),
                            'source': doc_info.get('source_file', doc_info.get('source', '')),
                            'date': f"{doc_info.get('year', '')}-{doc_info.get('month', '')}",
                            'keywords': doc_info.get('keywords', []),
                            'topics': doc_info.get('topics', [])
                        },
                        'retriever': self.name
                    }
                    standardized_results.append((doc_dict, float(score)))
            
            return standardized_results
            
        except Exception as e:
            print(f"Error in BM25 adapter: {e}")
            return []
    
    def get_name(self) -> str:
        """Return the name of this retriever"""
        return self.name