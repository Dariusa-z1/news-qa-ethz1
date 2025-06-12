
# 🧠 ETH News RAG System
**Multilingual Retrieval-Augmented Generation (RAG) with Hybrid Retrieval**

**Last Updated:** June 3, 2025  
**Branch:** `graph-rag-implementation`  
**Repository:** [news-qa-ethz1](https://github.com/Dariusa-z1/news-qa-ethz1)

---

## 📌 Executive Summary

This project implements a multilingual Retrieval-Augmented Generation (RAG) system for ETH news articles using a **hybrid retrieval approach**. It combines:

- **BM25** (lexical retrieval)
- **Dense retrieval with ChromaDB** (semantic search)
- **GraphRAG** (entity-aware retrieval via a knowledge graph)

Newly added: **Groq LLM integration** for answer synthesis from retrieved content.

---

## ✅ Key Features

- ✅ **Hybrid Architecture:** Lexical + Semantic + Graph-based retrieval
- ✅ **Multilingual Support:** Cross-lingual queries (EN/DE)
- ✅ **LLM Integration:** Groq LLM replaces GPT-2 for answer generation
- ✅ **Document Indexing:** 4,352 (BM25), 47,333 (Dense), 163 nodes (Graph)
- ✅ **Knowledge Graph:** 1,147 entity relationships
- ✅ **Production Ready:** All retrievers and Groq-based answer generation operational

---

## 🆕 Latest Updates

| Feature/Change                  | Status       |
|--------------------------------|--------------|
| `generate_answers_groq.py`     | ✅ Added      |
| `groq_generated_answers.json`  | ✅ Added      |
| Groq LLM Integration           | ✅ Successful |
| GPT-2                          | ❌ Deprecated |
| Answer Quality Issue           | ⚠️ Identified |

### 🔍 Insight:
Despite accurate **topic-level retrieval**, most answers lack **fact-level specificity** (e.g., dates, figures).  
90% of test questions correctly return: `"I cannot find this information"` — consistent with gaps in source documents.

---

## 📐 System Architecture

```text
                    Query Input
                           ↓
                ┌────────────────────┐
                │  Query Processing  │
                └────────────────────┘
                           ↓
     ┌────────────┬─────────────┬──────────────┐
     │   BM25     │   ChromaDB   │   GraphRAG   │
     │ Lexical    │ Semantic     │ Knowledge    │
     └────┬───────┴──────┬───────┴──────┬───────┘
          ↓              ↓              ↓
             →→→ Score Fusion (RRF) ←←←
                           ↓
                    Retrieved Docs
                           ↓
               ┌────────────────────┐
               │ Groq Answer Synthesis │
               └────────────────────┘
                           ↓
                   Final Answer Output


⸻

🏗️ Repository Structure

news-qa-ethz1/
├── HKNews/                            # Source news articles (EN/DE)
├── benchmark/                         # Evaluation Q&A pairs, benchmark scripts
├── bm25_query_results/                # BM25 retrieval outputs
├── graphrag/                          # Graph-based retriever module
├── hybrid_retrieval/                  # Core hybrid retriever logic
│   ├── adapters/                      # Wrapper modules for each retriever
│   ├── benchmark_qa.json              # Sample Q&A pairs
│   ├── hybrid_retriever.py	       # Orchestrates hybrid retrieval by combining BM25, Dense, and GraphRAG methods with optional score fusion and multi-model reranking.
│   ├── score_fusion.py		       # Implements RRF and weighted score fusion algorithms to combine results from multiple retrievers.
│   ├── reranking.py                   # Implements multi-model re-ranking using cross-encoders, ensemble RRF, summary-based, keyword boosting, and Cohere API.
│   ├── generate_answers_groq.py       # Groq LLM-based answer generation
│   ├── groq_generated_answers.json    # Generated answers 
│   ├── groq_top5_scores.json          # Top-5 retrieved results
│   ├── evaluation_results.json        # Evaluation metrics
│   ├── semantic_eval_results.json
│   ├── rag_pipeline.py 	       # Tests hybrid retrieval with and without reranking, and generates answers using top documents via GPT-2.
│   ├── evaluate_semantic_similarity.py # Evaluates retrieval quality using semantic similarity to ground-truth answers across baseline and reranked results.
│   └── test_hybrid.py                 # Runs and compares hybrid retrieval with and without reranking using real or sample data.
├── lib/                               # Supporting libraries (custom)
├── multilingual_bm25/                 # BM25 with multilingual support
├── notebooks/                         # Development notebooks
│   ├── chroma_db/                     # ChromaDB embeddings (two collections)
│   ├── parsed_markdown/               # Markdown-extracted article content
│   ├── processed_articles/            # Cleaned JSON articles w/ metadata
│   ├── 01_html_parsing_comparison.ipynb #  Compares BeautifulSoup and Docling for HTML parsing to optimize content extraction for RAG.
│   ├── 02_hybrid_parsing.ipynb	       # Implements a hybrid BeautifulSoup–Docling parser to robustly extract and clean HTML news content.
│   ├── 2_1_bm25_experiments.ipynb     # Multilingual BM25 retrieval with query translation for EN/DE search.
│   ├── 2_2_v2_updated_script.ipynb    # Dense Vector Retrieval + Chunking Analysis
│   ├── 2_5_pre_retrieval.ipynb	       # Implements query expansion, rewriting, and routing strategies to enhance retrieval precision and adaptability.
│   └── eth_benchmark_qa.json
├── scripts/                           # Utilities and helpers
├── .gitignore
├── .gitattributes
├── README.md                          # 🔹 Main project overview
├── requirements.txt                   # Python dependencies
├── debug_bm25.py
├── test_graphrag.py                   # Tests GraphRAG retrieval and graph visualization with sample data.
├── test_graph.html
├── knowledge_graph.html               # Visual graph output (static)
├── generate_answers_groq.py           # Uses Groq LLM to generate answers for benchmark questions using top retrieved documents.
└── entity_chunks_*.pickle             # Preprocessed entities for KG


⸻

⚙️ Installation & Setup

# Clone the project
git clone -b graph-rag-implementation https://github.com/Dariusa-z1/news-qa-ethz1.git
cd news-qa-ethz1

# Install dependencies
pip install -r requirements.txt
pip install rank-bm25 nltk

# NLTK resources
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run hybrid retrieval
python hybrid_retrieval/test_hybrid.py

# Run answer generation (Groq)
python generate_answers_groq.py


⸻

🧪 Evaluation Summary

Test Query Example: "artificial intelligence research at ETH"
	•	Topic Retrieval: ✅ Relevant articles retrieved
	•	Fact Retrieval: ⚠️ Many articles do not contain the exact answer
	•	Answer Generation: 90% return correct "Not found" response

Sample Result

{
  "question": "When did the InSight lander touch down on Mars?",
  "answer": "I cannot find this information in the documents retrieved."
}

Conclusion:

The system is robust in identifying relevant topics, but answer synthesis is limited by document content coverage.




⸻

💡 Lessons Learned
	•	Retrieval precision at topic level is strong (esp. with GraphRAG).
	•	Fact-level content is often missing from documents.
	•	Groq LLM accurately reflects when info is missing — a sign of robust generation logic.
	•	Improving retriever recall or content enrichment is key to better answers — but risky close to deadline.

⸻

🔭 Future Enhancements
	•	🧠 Query-Type Aware Weighting
	•	🗃️ Larger or enriched datasets (external sources)
	•	📌 Add reranking and summarization modules
	•	🔀 Distributed search for scalability
	•	📝 Result traceability + explanation

⸻

👨‍💻 Contributors
	•	Arnold Olympio
	•	Daria Onishchuk
	•	Yaqun Wu


⸻

📂 Appendix
	•	Repo: news-qa-ethz1
	•	Branch: graph-rag-implementation
	•	Last Commit: June 3, 2025
	•	Lines of Code: 2,000+
	•	Groq Answers: groq_generated_answers.json

⸻

🏁 Summary

The ETH News RAG system integrates three powerful retrieval methods and Groq LLM for robust, multilingual Q&A. While retrieval quality is strong at the topic level, the system faces fact-level recall limitations. Despite that, it showcases advanced architecture, production-ready components, and thoughtful evaluation—all critical to next-generation academic search engines.


