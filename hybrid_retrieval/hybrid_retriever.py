"""
Hybrid Retriever - Main orchestrator for combining multiple retrieval methods
"""
from typing import List, Dict, Any, Tuple, Optional, Union
from .adapters.bm25_adapter import BM25Adapter
from .adapters.dense_adapter import DenseAdapter
from .adapters.graphrag_adapter import GraphRAGAdapter
from .score_fusion import reciprocal_rank_fusion, weighted_fusion, normalize_scores


class HybridRetriever:
    """Main hybrid retrieval system combining BM25, Dense, and GraphRAG"""
    
    def __init__(self, 
                 bm25_adapter: Optional[BM25Adapter] = None,
                 dense_adapter: Optional[DenseAdapter] = None,
                 graphrag_adapter: Optional[GraphRAGAdapter] = None,
                 fusion_method: str = "rrf",
                 weights: List[float] = None):
        """
        Initialize hybrid retriever
        
        Args:
            bm25_adapter: BM25 retriever adapter
            dense_adapter: Dense/ChromaDB retriever adapter
            graphrag_adapter: GraphRAG retriever adapter
            fusion_method: Method to fuse scores ("rrf" or "weighted")
            weights: Weights for retrievers [bm25, dense, graphrag] (for weighted fusion)
        """
        self.retrievers = []
        self.retriever_names = []
        
        if bm25_adapter:
            self.retrievers.append(bm25_adapter)
            self.retriever_names.append("BM25")
        
        if dense_adapter:
            self.retrievers.append(dense_adapter)
            self.retriever_names.append("Dense")
            
        if graphrag_adapter:
            self.retrievers.append(graphrag_adapter)
            self.retriever_names.append("GraphRAG")
        
        if not self.retrievers:
            raise ValueError("At least one retriever must be provided")
        
        self.fusion_method = fusion_method
        self.weights = weights or [1.0 / len(self.retrievers)] * len(self.retrievers)
        
    def retrieve(self, query: str, top_k: int = 10, 
                 per_retriever_k: int = 20) -> List[Tuple[Dict, float]]:
        """
        Retrieve documents using hybrid approach
        
        Args:
            query: Search query
            top_k: Final number of results to return
            per_retriever_k: Number of results to get from each retriever
            
        Returns:
            Fused and re-ranked results
        """
        # Collect results from all retrievers
        all_results = []
        
        for retriever in self.retrievers:
            try:
                results = retriever.retrieve(query, top_k=per_retriever_k)
                all_results.append(results)
                print(f"{retriever.get_name()}: Retrieved {len(results)} results")
            except Exception as e:
                print(f"Error in {retriever.get_name()}: {str(e)}")
                all_results.append([])
        
        # Apply fusion
        if self.fusion_method == "rrf":
            fused_results = reciprocal_rank_fusion(all_results)
        elif self.fusion_method == "weighted":
            fused_results = weighted_fusion(all_results, self.weights)
        else:
            raise ValueError(f"Unknown fusion method: {self.fusion_method}")
        
        # Return top-k results
        return fused_results[:top_k]
    
    def print_results(self, results: List[Tuple[Dict, float]], max_content_length: int = 200):
        """Pretty print retrieval results"""
        print(f"\n{'='*80}")
        print(f"Hybrid Retrieval Results (Fusion: {self.fusion_method})")
        print(f"{'='*80}\n")
        
        for rank, (doc, score) in enumerate(results, 1):
            print(f"Rank {rank}: Score = {score:.4f}")
            print(f"Retriever: {doc.get('retriever', 'Unknown')}")
            print(f"Title: {doc.get('title', 'No title')}")
            
            content = doc.get('content', '')
            if len(content) > max_content_length:
                content = content[:max_content_length] + "..."
            print(f"Content: {content}")
            
            print(f"Metadata: {doc.get('metadata', {})}")
            print("-" * 80)