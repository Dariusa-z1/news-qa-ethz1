"""
Create benchmark dataset for ETH News RAG evaluation
Based on 25 questions provided by professor
"""
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hybrid_retrieval.hybrid_retriever import HybridRetriever
from hybrid_retrieval.adapters.bm25_adapter import BM25Adapter
from hybrid_retrieval.adapters.dense_adapter import DenseAdapter
from hybrid_retrieval.adapters.graphrag_adapter import GraphRAGAdapter
from typing import List, Dict, Any

# Professor's 25 benchmark questions with answers and scoring rules
BENCHMARK_QUESTIONS = [
    {
        "id": 1,
        "question": "Who was president of ETH in 2003?",
        "answer": "Olaf Kübler",
        "type": "factual",
        "scoring_notes": "Exact match required"
    },
    {
        "id": 2,
        "question": "Who were the rectors of ETH between 2017 and 2022?",
        "answer": "Sarah Springman, Günther Dissertori",
        "type": "factual_list",
        "scoring_notes": "0.5 points for listing only one rector"
    },
    {
        "id": 3,
        "question": "Who at ETH received ERC grants?",
        "answer": "ETH Zurich received hundreds of ERC grants over the years. What year or discipline are you interested in?",
        "answer_list": ["Tobias Donner", "Eliot Ash", "Ursula Keller", "Klaus Ensslin", "Yiwen Chu", 
                       "Judit Szulágyi", "Sebastiano Cantalupo", "Veerle Sterken", "Rachel Grange", 
                       "Paolo Crivelli", "Christian Degen", "Jonathan Home", "Lavinia Heisenberg", 
                       "Tilman Esslinger"],
        "type": "list_or_deflect",
        "scoring_notes": "Points = 1 – exp(–Score/5), +1 per correct, -1 per incorrect. OR 1 point for deflection answer"
    },
    {
        "id": 4,
        "question": "When did the InSight get to Mars?",
        "answer": "26 November 2018",
        "type": "factual",
        "scoring_notes": "Exact date required"
    },
    {
        "id": 5,
        "question": "What did Prof. Schubert say about flying?",
        "answer": "Flying is too cheap. If we want to reduce flying, surcharges on air fares are certainly a step in the right direction.",
        "type": "quote",
        "scoring_notes": "Should capture the essence of the quote"
    },
    {
        "id": 6,
        "question": "What is e-Sling?",
        "answer": "4-seated electric airplane, built by 20 electrical and mechanical engineering students at ETH Zurich",
        "type": "factual",
        "scoring_notes": "Should mention electric airplane and ETH students"
    },
    {
        "id": 7,
        "question": "Who are famous ETH alumni?",
        "answer_list": ["Wilhelm Conrad Röntgen", "Charles-Edouard Guillaume", "Albert Einstein", 
                       "Felix Bloch", "Heinrich Rohrer", "Georg Bednorz", "Karl Alexander Müller", 
                       "Alfred Werner", "Fritz Haber", "Richard Ernst", "Tadeus Reichstein", 
                       "Werner Arber", "Othmar Ammann", "Max Frisch", "Rudolf Clausius", 
                       "Santiago Calatrava", "John von Neumann", "Maurice Koechlin", "Mileva Marić"],
        "type": "list",
        "scoring_notes": "Points = 1 – exp(–Score/5), +1 for listed alumni, +0.5 for unlisted but valid, -1 for non-alumni"
    },
    {
        "id": 8,
        "question": "Who at ETH currently works on research regarding climate change?",
        "answer": "Multiple departments and initiatives including D-USYS, Institute for Atmospheric and Climate Science, Chair of Hydrology and Water Resources Development (D-BAUG), NADEL, and ETH Net Zero",
        "type": "research_overview",
        "scoring_notes": "Should mention multiple initiatives across research, policy, and institutional sides"
    },
    {
        "id": 9,
        "question": "How do alpine plants respond to climate change?",
        "answer": "Alpine plants struggle with competition from lower-elevation species migrating upward due to warming, rather than the warming itself. This gradually alters plant communities, especially at mid-elevations.",
        "type": "research_explanation",
        "scoring_notes": "Should explain the phenomenon based on ETH research"
    },
    {
        "id": 10,
        "question": "How would you make fertilizer without carbon emissions?",
        "answer": "Options include electrification using renewable energy for hydrogen production via water electrolysis, hydrogen from biomass, improving fertilizer efficiency, and decentralized production in regions with abundant renewables.",
        "type": "research_explanation",
        "scoring_notes": "Should explain multiple approaches based on ETH research"
    },
    {
        "id": 11,
        "question": "What research is ETH famous for?",
        "answer": "As a research-intensive university, ETH conducts research across a wide spectrum of disciplines. What are you interested in?",
        "type": "deflection",
        "scoring_notes": "Must deflect without favoring any department"
    },
    {
        "id": 12,
        "question": "How much of ETH's electricity consumption is due to computing? How did that develop over the years?",
        "answer": "We have very little data on this. In 2017, computing at ETH Zurich produced 13,500 tons of CO2, about 10% of total emissions. ETH consumes about 40 GWh of electricity per year, increasing over time. ETH has a Net-Zero emissions goal by 2030.",
        "type": "data_admission",
        "scoring_notes": "Must start with 'we do not know' or similar, then provide related information"
    },
    {
        "id": 13,
        "question": "What are pseudocereals and who does research on them?",
        "answer": "Pseudocereals are plants not botanically related to true cereals but used similarly. They offer pest resistance, high nutritional value, and are gluten-free. The three most important are buckwheat, quinoa, and amaranth. The Molecular Plant Breeding group at ETH Zurich works on this.",
        "type": "research_explanation",
        "scoring_notes": "Should define pseudocereals and mention the research group"
    },
    {
        "id": 14,
        "question": "Who is working on methods for targeted cancer treatment, and what do they use?",
        "answer": "Multiple groups: tumor-targeted radioligands using solid-phase chemistry, Daniel Richter improving drug-antibody linkages, Professor Bernd Bodenmiller at Tumor Profiler Center using big data, and Engimmune Therapeutics engineering T-cell receptors.",
        "type": "research_collection",
        "scoring_notes": "Should collect and summarize multiple research efforts"
    },
    {
        "id": 15,
        "question": "How is ETH research investigating methods to avoid diarrhea?",
        "answer": "Emma Slack's team showed vaccine-induced IgA antibodies trap bacteria in clumps, preventing infection without killing them. This blocks genetic exchange and antibiotic resistance spread. Tested with oral vaccines from inactivated Salmonella and E. coli.",
        "type": "research_explanation",
        "scoring_notes": "Should explain the research mechanism"
    },
    {
        "id": 16,
        "question": "What is ETH Plus?",
        "answer": "Two meanings: 1) PLUS - Planning Landscape and Urban Settings (D-BAUG initiative), 2) ETH+ - 2017 Executive Board program for unconventional approaches, renamed Open ETH in 2019",
        "type": "disambiguation",
        "scoring_notes": "Must mention both meanings"
    },
    {
        "id": 17,
        "question": "How do birds learn new songs?",
        "answer": "Songbirds learn incrementally by adapting known syllables to new ones, initially jumbled then rearranged correctly. Similar to computer linguistics algorithms and possibly human language acquisition. ETH Zurich studied this in zebra finches.",
        "type": "research_explanation",
        "scoring_notes": "Should explain the learning process based on ETH research"
    },
    {
        "id": 18,
        "question": "What connections does ETH have to Hong Kong?",
        "answer": "Student/researcher exchange plus institutional agreements with CUHK (Joint Research Lab, Chow Yuk Ho Technology Centre), HKUST Schools of Engineering & Science. Recent remote endoscopy with CUHK.",
        "type": "institutional",
        "scoring_notes": "Should mention specific partnerships"
    },
    {
        "id": 19,
        "question": "For how many years has ETH done research on Quantum Computing?",
        "answer": "ETH research on quantum electronics goes back to 1988. In 2021, ETH and Paul Scherrer Institute founded the Quantum Computing Hub.",
        "type": "factual",
        "scoring_notes": "Should mention 1988 start date"
    },
    {
        "id": 20,
        "question": "What are the current projections for the student numbers at ETH?",
        "answer": "In 2022, ETH Zurich was projecting an increase in student and doctoral student numbers of approximately 3.5% per year both for 2021–2024 and for 2025–2028.",
        "type": "factual",
        "scoring_notes": "Should mention 3.5% annual growth projection"
    },
    {
        "id": 21,
        "question": "Why should I study at ETH?",
        "answer": "ETH Zurich is a top global university with outstanding education, pioneering research, and strong industry connections. 25,000+ students from 120+ countries, 20+ Nobel laureates, 540+ spin-offs, located in Switzerland's thriving economy.",
        "type": "promotional",
        "scoring_notes": "Should highlight key strengths without being overly promotional"
    },
    {
        "id": 22,
        "question": "Who investigated the catastrophic events in Tibet in 2016, and what was found?",
        "answer": "International team from ETH Zurich, SLF/WSL, GAPHAZ found glacier in 'surging' state with meltwater accumulation causing collapse. First collapse July 17 killed 9 herders. Team predicted and warned about second collapse Sept 22.",
        "type": "research_explanation",
        "scoring_notes": "Should explain the investigation and findings"
    },
    {
        "id": 23,
        "question": "Why should ETH receive any additional funding?",
        "answer": "Additional funding for ETH Zurich is an investment in innovation, education, and the future, enabling transformative research, nurturing global talent, and driving economic and societal progress with lasting benefits.",
        "type": "deflection",
        "scoring_notes": "Should deflect to higher education in general, not compare to other universities"
    },
    {
        "id": 24,
        "question": "Anybody at ETH doing anything for people with disabilities?",
        "answer": "ETH's Barrier-Free ETH initiative aims for 'Design for all' principle for unrestricted access to buildings and services. Various research projects on assistive technology.",
        "type": "institutional",
        "scoring_notes": "Should mention both accessibility initiatives and research"
    },
    {
        "id": 25,
        "question": "Does ETH organize any competitions?",
        "answer": "ETH Zurich organizes competitions for youth, aspiring researchers, sports, innovators, and entrepreneurs. What area would you like to explore?",
        "type": "deflection",
        "scoring_notes": "Should deflect, could mention CYBATHLON if asked specifically"
    }
]

def label_document_relevance(document: Dict[str, Any], question: Dict[str, Any]) -> float:
    """
    Label a document's relevance to a question based on content matching
    Returns: 1.0 (complete answer), 0.5 (partial answer), 0.0 (not relevant)
    """
    doc_content = document.get('content', '').lower()
    doc_title = document.get('title', '').lower()
    full_text = f"{doc_title} {doc_content}"
    
    # Check for answer presence
    answer = question.get('answer', '').lower()
    
    # For list questions, check individual items
    if question['type'] in ['factual_list', 'list', 'list_or_deflect']:
        answer_list = question.get('answer_list', [])
        if answer_list:
            matches = sum(1 for item in answer_list if item.lower() in full_text)
            if matches >= len(answer_list) * 0.5:
                return 1.0
            elif matches > 0:
                return 0.5
    
    # For regular questions, check answer presence
    if answer and answer in full_text:
        return 1.0
    
    # Check for partial matches based on keywords
    keywords = extract_keywords(question['question'])
    keyword_matches = sum(1 for kw in keywords if kw.lower() in full_text)
    
    if keyword_matches >= len(keywords) * 0.7:
        return 0.5
    elif keyword_matches >= len(keywords) * 0.3:
        return 0.5
    
    return 0.0

def extract_keywords(question: str) -> List[str]:
    """Extract important keywords from a question"""
    # Remove common question words
    stop_words = {'who', 'what', 'when', 'where', 'why', 'how', 'is', 'are', 
                  'was', 'were', 'did', 'does', 'do', 'the', 'at', 'in', 'on'}
    
    words = question.lower().split()
    keywords = [w for w in words if w not in stop_words and len(w) > 2]
    
    return keywords

def create_benchmark():
    """Create benchmark dataset by retrieving and labeling documents for each question"""
    print("Initializing retrievers...")
    
    # Initialize individual retrievers
    bm25 = None
    dense = None
    graphrag = None
    
    try:
        bm25 = BM25Adapter()
        print("✓ BM25 initialized")
    except Exception as e:
        print(f"✗ BM25 failed: {e}")
    
    try:
        dense = DenseAdapter()
        print("✓ Dense retriever initialized")
    except Exception as e:
        print(f"✗ Dense retriever failed: {e}")
    
    try:
        graphrag = GraphRAGAdapter()
        print("✓ GraphRAG initialized")
    except Exception as e:
        print(f"✗ GraphRAG failed: {e}")
    
    # Initialize hybrid retriever with the available retrievers
    retriever = HybridRetriever(
        bm25_adapter=bm25,
        dense_adapter=dense,
        graphrag_adapter=graphrag,
        fusion_method="rrf"
    )
    
    # Count how many retrievers are active
    active_retrievers = sum(1 for r in [bm25, dense, graphrag] if r is not None)
    print(f"Hybrid retriever initialized with {active_retrievers} retrievers")
    
    benchmark = {
        "metadata": {
            "version": "1.0",
            "created": "2025-06-03",
            "total_questions": 25,
            "question_types": {
                "factual": [1, 4, 6, 19, 20],
                "list": [2, 3, 7],
                "research_explanation": [9, 10, 13, 15, 17, 22],
                "deflection": [11, 23, 25],
                "other": [5, 8, 12, 14, 16, 18, 21, 24]
            }
        },
        "questions": []
    }
    
    for q in BENCHMARK_QUESTIONS:
        print(f"\nProcessing Question {q['id']}: {q['question']}")
        
        # Retrieve documents
        try:
            results = retriever.retrieve(q['question'], top_k=50)
            print(f"Retrieved {len(results)} documents")
            
            # Label documents
            labeled_docs = []
            for doc, score in results[:20]:  # Focus on top 20
                relevance = label_document_relevance(doc, q)
                if relevance > 0:  # Only keep relevant documents
                    labeled_docs.append({
                        "doc_id": doc.get('id', 'unknown'),
                        "title": doc.get('title', '')[:100],
                        "relevance_score": relevance,
                        "retrieval_score": score,
                        "retriever": doc.get('retriever', 'unknown')
                    })
            
            # Sort by relevance score
            labeled_docs.sort(key=lambda x: x['relevance_score'], reverse=True)
            
            print(f"Found {len(labeled_docs)} relevant documents")
            
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            labeled_docs = []
        
        # Add to benchmark
        benchmark["questions"].append({
            "id": q['id'],
            "question": q['question'],
            "answer": q.get('answer', ''),
            "answer_list": q.get('answer_list', []),
            "type": q['type'],
            "scoring_notes": q['scoring_notes'],
            "relevant_documents": labeled_docs[:10]  # Keep top 10 relevant
        })
    
    # Save benchmark
    output_path = "hybrid_retrieval/benchmark_qa.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(benchmark, f, indent=2, ensure_ascii=False)
    
    print(f"\nBenchmark saved to {output_path}")
    print(f"Total questions: {len(benchmark['questions'])}")
    
    # Print summary
    total_relevant = sum(len(q['relevant_documents']) for q in benchmark['questions'])
    print(f"Total relevant documents found: {total_relevant}")
    
    return benchmark

if __name__ == "__main__":
    create_benchmark()
