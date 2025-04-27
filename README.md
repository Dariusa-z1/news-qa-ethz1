# 📰 News QA ETHZ - RAG System

Welcome! This project is part of the *Advanced Generative AI* course at HSLU, in collaboration with ETH Zurich and Google DeepMind.

## ✨ Goal
Build a **Retrieval-Augmented Generation (RAG)** system that answers questions using ETH Zurich news articles.

## 🔄 Steps
- **Data Preparation**: Parsing and cleaning German and English news articles.
- **RAG Development**: Implementing BM25, Dense Retrieval, GraphRAG, or Hybrid retrieval.
- **Evaluation**: Automated and human-based answer evaluation.

## 🔹 Project Structure
```
news-qa-ethz/
├── HKNews/          # Raw news HTML files
├── data/            # Cleaned dataset (coming soon)
├── retrievers/      # Retrieval methods (coming soon)
├── rerankers/       # Re-ranking models (coming soon)
├── notebooks/       # Data processing and experiments
├── README.md
├── requirements.txt # To be added
├── .gitignore
└── venv/            # Virtual environment (ignored)
```

## 📚 Setup
```bash
git clone https://github.com/Dariusa-z1/news-qa-ethz1.git

cd news-qa-ethz

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## 📓 Notes
- Project is under active development.
- Individual contributions will be documented.

---
❤️ ETH Zurich | HSLU | Google DeepMind | 2025

