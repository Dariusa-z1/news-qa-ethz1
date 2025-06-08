from pathlib import Path
import json
import requests
import re
import time

# === Configuration ===
GROQ_API_KEY = "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"  
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
RESULTS_DIR = Path(__file__).resolve().parent.parent / "notebooks" / "bm25_results"

OUTPUT_FILE = Path("groq_top5_scores.json")
# Ensure the output directory exists
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# === Groq LLM Request ===
def ask_groq(question, reference, document_text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    prompt = f"""
You are evaluating whether a retrieved document correctly answers a benchmark question.

QUESTION:
{question}

REFERENCE ANSWER:
{reference}

RETRIEVED DOCUMENT:
{document_text[:3000]}

SCORING RULE:
- Score 1.0 if the document fully answers the question
- Score 0.5 if it gives a partial answer (some info is missing)
- Score 0.0 if it is irrelevant or wrong

Respond only in this format:
Score: X
Without any explanation, just the score.
"""

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


# === Retry Wrapper ===
def safe_groq_call(question, reference, document_text, retries=5, delay=10):
    for attempt in range(retries):
        try:
            return ask_groq(question, reference, document_text)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                wait_time = delay * (2 ** attempt)  # 10s, 20s, 40s, ...
                print(f"429 Rate limit hit. Waiting {wait_time} seconds before retry {attempt + 1}/{retries}")
                time.sleep(wait_time)
            else:
                raise
    return "ERROR: Too many retries due to repeated 429 errors"

# === Run for top-5 documents per question ===
def store_groq_top5_scores():
    all_scores = []

    for file in RESULTS_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            entry = json.load(f)

        question = entry["query"]
        reference = entry["reference_answer"]
        if not entry["results"]:
            continue

        scored_results = []
        for i, res in enumerate(entry["results"][:5]):
            doc_text = res.get("main_content") or res.get("summary") or res.get("content_snippet", "")
            print(f"→ [{file.name}] Rank {i+1}")

            score_text = safe_groq_call(question, reference, doc_text)

            scored_results.append({
                "rank": i + 1,
                "title": res.get("title", ""),
                "score": res.get("score", 0),
                "document_text": doc_text,
                "groq_response": score_text
            })
        # Pause after evaluating this full question (top-5 done)
        time.sleep(10)
        
        all_scores.append({
            "file": file.name,
            "question": question,
            "reference_answer": reference,
            "results": scored_results
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_scores, f, indent=2, ensure_ascii=False)

    print(f" Saved all Groq top-5 scores to: {OUTPUT_FILE}")

if __name__ == "__main__":
    store_groq_top5_scores()

