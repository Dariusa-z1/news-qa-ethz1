# Semantic Retrieval Results - Version 1 (Initial Implementation)

This directory contains the complete set of retrieval results, ground truth annotations, and evaluation metrics for the first implementation of the ETH Zürich news semantic retrieval system.

## ⚠️ Note
These results were not satisfactory and the retrieval method is being redesigned from scratch.

## Files Overview:

### Original Retrieval Results:
- `semantic_search_fixed_results.json`: Raw retrieval results using fixed-size chunks
- `semantic_search_semantic_results.json`: Raw retrieval results using semantic chunks

### Ground Truth Files:
- `ground_truth_fixed.json`: GPT-4 generated relevance scores for fixed-size chunks
- `ground_truth_semantic.json`: GPT-4 generated relevance scores for semantic chunks

### Evaluation Reports:
- `evaluation_report_fixed.json`: Comprehensive evaluation metrics for fixed chunks
- `evaluation_report_semantic.json`: Comprehensive evaluation metrics for semantic chunks

### Analysis Files:
- `similarity_analysis.json`: Detailed analysis comparing similarity scores between chunk methods
- `benchmark_comparison_summary.json`: Overall comparison summary between chunk methods

### Visualizations:
- `retrieval_comparison.png`: Performance metrics comparison visualization

### Temporary Files:
- `*_temp_*.json`: Checkpoint files created during ground truth generation

## Technical Details:

### Retrieval Setup:
- **Embedding Model**: paraphrase-multilingual-MiniLM-L12-v2
- **Vector Database**: ChromaDB
- **Chunking Methods**: 
  - Fixed-size: 200 words with 50-word overlap
  - Semantic: Paragraph-based clustering using embedding similarity
- **Distance Metric**: Euclidean distance (converted to similarity using 1/(1+distance))

### Evaluation Metrics:
- **Precision@k**: Fraction of retrieved documents that are relevant (k=1,3,5)
- **Recall@k**: Fraction of all relevant documents retrieved (k=1,3,5)
- **MRR**: Mean Reciprocal Rank
- **NDCG@k**: Normalized Discounted Cumulative Gain (k=1,3,5)

### Ground Truth Scoring:
- **1.0**: Document fully answers the question with comprehensive information
- **0.5**: Document partially answers the question with some relevant information
- **0.0**: Document does not answer the question or is not relevant

### Issues Identified:
- Retrieval performance not meeting expectations
- Need to improve chunking strategy
- Potential issues with embedding quality or search parameters
- Requires complete redesign of retrieval methodology

## Next Steps:
- Implement improved retrieval method (Version 2)
- Experiment with different embedding models
- Optimize chunking strategies
- Consider hybrid retrieval approaches

---
*Generated on: 2025-05-14 10:46:51*
*Status: Archived - Superseded by Version 2*
