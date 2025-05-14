import json
import os
import networkx as nx
from graphrag.entity_extractor import EntityExtractor
from graphrag.graph_builder import GraphBuilder
from graphrag.graph_visualizer import GraphVisualizer
from graphrag.graph_rag_retriever import GraphRAGRetriever
from graphrag.evaluation import GraphRAGEvaluator

def load_test_data(sample_size=3):
    """Load sample data from JSON files if available,
    or create some test data if not available."""
    
    # Try to load data from a data directory
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    
    if os.path.exists(data_dir):
        json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]
        
        if json_files:
            print(f"Loading data from {len(json_files)} JSON files in {data_dir}")
            articles = []
            
            for i, file_name in enumerate(json_files[:sample_size]):
                file_path = os.path.join(data_dir, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Make sure to add an id if not present
                        if 'id' not in data:
                            data['id'] = i
                        articles.append(data)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
            
            return articles
    
    # If no data or loading fails, create synthetic test data
    print("No data found, creating test data")
    return [
        {
            "id": 1,
            "title": "ETH AI Research Breakthrough",
            "content": "ETH Zurich researchers have developed a new AI model. Professor Smith leads the project.",
            "language": "en",
            "date": "2023-01-15"
        },
        {
            "id": 2,
            "title": "KI-Forschung an der ETH",
            "content": "Die Forscher der ETH Zürich haben ein neues KI-Modell entwickelt. Professor Smith leitet das Projekt.",
            "language": "de",
            "date": "2023-01-20"
        },
        {
            "id": 3,
            "title": "Climate Research Initiative",
            "content": "ETH Zurich launched a new climate research initiative. The initiative aims to develop new technologies to combat climate change.",
            "language": "en",
            "date": "2023-02-15"
        }
    ]

def main():
    """Main test function"""
    print("Testing GraphRAG implementation...")
    
    # Load test data
    articles = load_test_data()
    print(f"Loaded {len(articles)} test articles")
    
    # Initialize components
    print("\nInitializing components...")
    extractor = EntityExtractor()
    builder = GraphBuilder(extractor)
    visualizer = GraphVisualizer()
    
    # Build knowledge graph
    print("\nBuilding knowledge graph...")
    G, entity_chunks = builder.create_knowledge_graph(articles)
    G = builder.add_temporal_edges(G, articles)
    G = builder.add_topic_edges(G, articles)
    
    print(f"Created graph with {len(G.nodes())} nodes and {len(G.edges())} edges")
    
    # Visualize graph
    print("\nVisualizing graph...")
    html_file = visualizer.visualize_interactive(G, output_file="test_graph.html")
    print(f"Interactive visualization saved to {html_file}")
    
    # Initialize retriever
    print("\nInitializing retriever...")
    retriever = GraphRAGRetriever(G)
    
    # Store documents in ChromaDB
    print("\nStoring documents in ChromaDB...")
    try:
        retriever.store_documents(articles, entity_chunks)
        print("Documents stored successfully")
    except Exception as e:
        print(f"Error storing documents: {e}")
    
    # Test retrieval
    print("\nTesting retrieval...")
    test_queries = [
        "What research is happening at ETH Zurich?",
        "Who is Professor Smith?",
        "Tell me about climate research"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = retriever.retrieve(query, top_k=2)
        
        print(f"Retrieved {len(results)} results:")
        for i, result in enumerate(results):
            print(f"\nResult {i+1}:")
            print(f"ID: {result['id']}")
            print(f"Score: {result.get('score', 0):.4f}")
            if 'expansion_level' in result:
                print(f"Expansion Level: {result['expansion_level']}")
            # Print a snippet of the text
            text_snippet = result['text'][:150] + "..." if len(result['text']) > 150 else result['text']
            print(f"Text: {text_snippet}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
