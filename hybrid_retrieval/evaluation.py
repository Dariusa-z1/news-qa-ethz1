# evaluation.py
class RAGEvaluator:
    def __init__(self, benchmark_path):
        self.benchmark = load_benchmark(benchmark_path)
    
    def evaluate_retrieval(self, retriever):
        """Calculate Precision@k, Recall@k, MRR"""
        metrics = {
            "precision@5": [],
            "recall@5": [],
            "mrr": [],
            "per_question_scores": []
        }
        
        for question in self.benchmark["questions"]:
            results = retriever.retrieve(question["question"])
            metrics = calculate_metrics(results, question["relevant_docs"])
        
        return aggregate_metrics(metrics)
    
    def evaluate_answers(self, rag_system):
        """Score actual answers using professor's rubric"""
        scores = []
        
        for q in self.benchmark["questions"]:
            answer = rag_system.generate_answer(q["question"])
            score = score_answer(answer, q)  # Apply specific scoring rules
            scores.append(score)
        
        return sum(scores)  # Total out of 25
