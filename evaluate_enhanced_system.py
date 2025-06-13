import json
from hybrid_retrieval.enhanced_hybrid_retriever import EnhancedHybridRetriever
from hybrid_retrieval.adapters.bm25_adapter import BM25Adapter
from hybrid_retrieval.adapters.dense_adapter import DenseAdapter
from hybrid_retrieval.adapters.graphrag_adapter import GraphRAGAdapter

# Load benchmark
with open('hybrid_retrieval/benchmark_qa.json', 'r') as f:
    data = json.load(f)
    questions = data['questions']

# Initialize enhanced system
print("Initializing enhanced retrieval system...")
bm25 = BM25Adapter()
dense = DenseAdapter()
graphrag = GraphRAGAdapter()

hybrid = EnhancedHybridRetriever(
    bm25_adapter=bm25,
    dense_adapter=dense,
    graphrag_adapter=graphrag,
    fusion_method='rrf',
    use_reranking=True
)

# Test key questions
test_questions = [1, 4, 5, 6]  # Questions we've been working on
results = []

print("\nEvaluating key questions with enhanced system:")
print("="*60)

for q in questions:
    if q['id'] not in test_questions:
        continue
        
    print(f"\nQ{q['id']}: {q['question']}")
    
    # Retrieve with enhanced system
    retrieval_results = hybrid.retrieve(q['question'], top_k=10, per_retriever_k=30)
    
    # Check if answer is in results
    found = False
    found_in = None
    
    for i, (doc, score) in enumerate(retrieval_results[:5]):
        content = str(doc.get('content', '')).lower()
        
        if q['id'] == 1 and 'olaf kübler' in content:
            found = True
            found_in = i + 1
            break
        elif q['id'] == 4 and '26 november 2018' in content:
            found = True
            found_in = i + 1
            break
        elif q['id'] == 5 and 'schubert' in content and ('cheap' in content or 'flying' in content):
            found = True
            found_in = i + 1
            break
        elif q['id'] == 6 and ('e-sling' in content or 'esling' in content):
            found = True
            found_in = i + 1
            break
    
    result = {
        'question_id': q['id'],
        'question': q['question'],
        'answer_found': found,
        'found_in_position': found_in,
        'expected_answer': q['answer']
    }
    results.append(result)
    
    if found:
        print(f"✓ Answer found in position {found_in}")
    else:
        print("✗ Answer not found in top 5")

# Save results
with open('enhanced_evaluation_results.json', 'w') as f:
    json.dump(results, f, indent=2)

# Summary
successful = sum(1 for r in results if r['answer_found'])
print(f"\n{'='*60}")
print(f"Enhanced System Results: {successful}/{len(results)} questions answered")
print(f"Success Rate: {successful/len(results)*100:.0f}%")
print("\nResults saved to enhanced_evaluation_results.json")
