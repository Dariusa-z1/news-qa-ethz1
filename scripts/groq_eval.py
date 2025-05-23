from pathlib import Path
import json
import requests
import re

# Configuration
GROQ_API_KEY = "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"  # Replace with your actual API key
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
RESULTS_DIR = Path(__file__).resolve().parent.parent / "notebooks" / "bm25_results"

OUTPUT_FILE = Path("groq_raw_answers.json")
# Ensure the output directory exists
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Function to call Groq LLM
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

# Main function
def store_groq_answers():
    evaluations = []

    for file in RESULTS_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            entry = json.load(f)

        question = entry["query"]
        reference = entry["reference_answer"]
        top_result = entry["results"][0] if entry["results"] else None
        if not top_result:
            continue

        doc_text = top_result.get("main_content") or top_result.get("summary") or top_result.get("content_snippet", "")

        print(f"→ Asking Groq for: {file.name}")
        try:
            response = ask_groq(question, reference, doc_text)
        except Exception as e:
            response = f"ERROR: {str(e)}"

        evaluations.append({
            "file": file.name,
            "question": question,
            "reference_answer": reference,
            "document_text": doc_text,
            "groq_response": response
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(evaluations, f, indent=2, ensure_ascii=False)

    print(f"Saved all Groq responses to {OUTPUT_FILE}")

if __name__ == "__main__":
    store_groq_answers()