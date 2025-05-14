# Ground Truth and Evaluation Results - Version 1

This directory contains the ground truth annotations and evaluation results for the ETH Zürich news retrieval system.

## Files:

### Ground Truth Files:
- `ground_truth_fixed.json`: Ground truth relevance scores for fixed-size chunks
- `ground_truth_semantic.json`: Ground truth relevance scores for semantic chunks

### Evaluation Reports:
- `evaluation_report_fixed.json`: Comprehensive evaluation metrics for fixed chunks
- `evaluation_report_semantic.json`: Comprehensive evaluation metrics for semantic chunks
- `similarity_analysis.json`: Analysis comparing similarity scores between chunk methods

### Summary Files:
- `benchmark_comparison_summary.json`: Overall comparison summary between chunk methods
- `retrieval_comparison.png`: Visualization comparing performance metrics

### Temporary Files:
- `*_temp_*.json`: Checkpoint files created during ground truth generation

## Evaluation Metrics:
- **Precision@k**: Fraction of retrieved documents that are relevant
- **Recall@k**: Fraction of all relevant documents retrieved
- **MRR**: Mean Reciprocal Rank
- **NDCG@k**: Normalized Discounted Cumulative Gain

## Ground Truth Scores:
- **1.0**: Document fully answers the question
- **0.5**: Document partially answers the question
- **0.0**: Document is not relevant to the question

Generated using GPT-4 for relevance assessment.
