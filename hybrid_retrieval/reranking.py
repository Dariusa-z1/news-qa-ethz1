"""
Re-ranking module for improving retrieval results
"""
from sentence_transformers import CrossEncoder
import numpy as np
from typing import List, Dict, Tuple, Any


class SimpleReranker:
    """Cross-encoder based re-ranker for document relevance scoring"""
    
    def __init__(self, model_name: str = 'cross-encoder/ms-marco-TinyBERT-L-2-v2'):
        """
        Initialize the re-ranker
        
        Args:
            model_name: HuggingFace model name for cross-encoder
        """
        print(f"Loading cross-encoder model: {model_name}")
        self.model = CrossEncoder(model_name)
        self.model_name = model_name
        print("Reranker model loaded successfully!")
        
    def rerank(self, query: str, results: List[Tuple[Dict, float]], top_k: int = 10) -> List[Tuple[Dict, float]]:
        """
        Rerank retrieval results using cross-encoder
        
        Args:
            query: Search query
            results: List of (document, score) tuples from retrieval
            top_k: Number of top documents to return after reranking
            
        Returns:
            List of reranked (document, rerank_score) tuples
        """
        if not results:
            return []
            
        print(f"Reranking {len(results)} documents for query: '{query[:50]}...'")
        
        # Extract documents and prepare query-document pairs
        documents = [doc for doc, _ in results]
        pairs = []
        
        for doc in documents:
            # Get content from document
            content = self._extract_content(doc)
            # Truncate very long content to avoid memory issues
            if len(content) > 512:
                content = content[:512]
            pairs.append([query, content])
        
        # Get relevance scores from cross-encoder
        rerank_scores = self.model.predict(pairs)
        
        # Sort by rerank scores (highest first) and get top_k
        scored_results = [(documents[i], float(rerank_scores[i])) for i in range(len(documents))]
        scored_results.sort(key=lambda x: x[1], reverse=True)
        
        reranked_results = scored_results[:top_k]
        
        # Add rerank score to document metadata
        for doc, score in reranked_results:
            doc['rerank_score'] = score
            doc['reranked_by'] = self.model_name
        
        print(f"✓ Reranking complete. Top score: {reranked_results[0][1]:.3f}")
        
        return reranked_results
    
    def _extract_content(self, doc: Dict) -> str:
        """Extract text content from document for reranking"""
        content_fields = ['content', 'text', 'chunk_text', 'body']
        
        for field in content_fields:
            if field in doc and doc[field]:
                return str(doc[field])
        
        return str(doc)


# Test function
if __name__ == "__main__":
    # Test the reranker
    reranker = SimpleReranker()
    
    # Sample query and results (mimicking your hybrid retriever output)
    query = "artificial intelligence research at ETH"
    
    # Mock results in your format: List[Tuple[Dict, float]]
    sample_results = [
        ({"content": "ETH Zurich is conducting groundbreaking AI research in machine learning.", "title": "AI Research"}, 0.5),
        ({"content": "The weather in Zurich is nice today.", "title": "Weather"}, 0.3),
        ({"content": "ETH researchers published a new paper on quantum computing.", "title": "Quantum Research"}, 0.4),
        ({"content": "Zurich is a beautiful city in Switzerland.", "title": "City Guide"}, 0.2),
        ({"content": "ETH's computer science department focuses on robotics and AI.", "title": "CS Department"}, 0.6)
    ]
    
    print("="*60)
    print("RERANKING TEST")
    print("="*60)
    print(f"Query: {query}")
    print(f"Original results: {len(sample_results)}")
    
    # Rerank documents
    reranked = reranker.rerank(query, sample_results, top_k=3)
    
    print(f"\nTop {len(reranked)} reranked results:")
    for i, (doc, score) in enumerate(reranked):
        print(f"\n{i+1}. Rerank Score: {score:.3f}")
        print(f"   Title: {doc['title']}")
        print(f"   Content: {doc['content']}")