"""Test script for hybrid retrieval system"""
import sys
import os

# Add parent directory to path to find multilingual_bm25
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hybrid_retrieval.adapters.bm25_adapter import BM25Adapter
from hybrid_retrieval.adapters.dense_adapter import DenseAdapter
from hybrid_retrieval.adapters.graphrag_adapter import GraphRAGAdapter
from hybrid_retrieval.hybrid_retriever import HybridRetriever


def main():
    print("Initializing Hybrid Retrieval System...")
    
    # Initialize adapters with error handling
    adapters = []
    
    try:
        print("\n1. Initializing BM25...")
        bm25 = BM25Adapter()
        adapters.append(bm25)
        print("✓ BM25 initialized successfully")
    except Exception as e:
        print(f"✗ BM25 initialization failed: {e}")
        bm25 = None
    
    try:
        print("\n2. Initializing Dense/ChromaDB...")
        dense = DenseAdapter()
        adapters.append(dense)
        print("✓ Dense retriever initialized successfully")
    except Exception as e:
        print(f"✗ Dense retriever initialization failed: {e}")
        dense = None
    
    try:
        print("\n3. Initializing GraphRAG...")
        graphrag = GraphRAGAdapter()
        adapters.append(graphrag)
        print("✓ GraphRAG initialized successfully")
    except Exception as e:
        print(f"✗ GraphRAG initialization failed: {e}")
        graphrag = None
    
    if not adapters:
        print("\nError: No retrievers could be initialized!")
        return
    
    # Create hybrid retriever with available adapters
    print(f"\n4. Creating Hybrid Retriever with {len(adapters)} retrievers...")
    hybrid = HybridRetriever(
        bm25_adapter=bm25,
        dense_adapter=dense,
        graphrag_adapter=graphrag,
        fusion_method="rrf"
    )
    
    # Test query
    query = "artificial intelligence research at ETH"
    print(f"\nTest Query: '{query}'")
    
    try:
        results = hybrid.retrieve(query, top_k=5)
        hybrid.print_results(results)
    except Exception as e:
        print(f"Error during retrieval: {e}")


if __name__ == "__main__":
    main()