import os
import json
import re
import string
import unicodedata
import logging
from tqdm import tqdm
from langdetect import detect

# Set up logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function 1: Basic Text Cleaning
def basic_text_cleaning(text):
    """
    Perform basic text cleaning operations.
    """
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKC', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text

# Function 2: Language Detection
def detect_language(text):
    """
    Detect the language of the given text.
    """
    if not text:
        return "unknown"
        
    try:
        # Use only the first 1000 characters for faster detection
        sample = text[:1000]
        language = detect(sample)
        return language
    except:
        # Default to unknown if detection fails
        return "unknown"

# Function 3: Extract Article Structure
def extract_article_structure(markdown_text):
    """
    Extract article structure from markdown text.
    """
    # Initialize article structure
    article = {
        'original_filename': '',
        'sections': {},
    }
    
    # Extract original filename from the header line
    header_match = re.search(r'^# (.+?)$', markdown_text, re.MULTILINE)
    if header_match:
        article['original_filename'] = header_match.group(1).strip()
    
    # Extract sections using line-by-line parsing
    lines = markdown_text.split('\n')
    current_section = None
    section_content = []
    
    for line in lines:
        if line.startswith('## '):
            # Save previous section if exists
            if current_section is not None:
                article['sections'][current_section] = '\n'.join(section_content).strip()
            
            # Start new section
            current_section = line[3:].strip()  # Remove '## ' prefix
            section_content = []
        elif current_section is not None:
            section_content.append(line)
    
    # Save the last section
    if current_section is not None and section_content:
        article['sections'][current_section] = '\n'.join(section_content).strip()
    
    return article

# Function 4: Extract Title
def extract_title(article_dict, filename):
    """
    Extract title from the article structure or filename.
    Keep in original language.
    """
    # First try to extract from content sections
    title_sections = ["In brief", "Main article", "Title", "Headline", "Titel", "Überschrift", "Kurz gefasst"]
    
    for section_name in title_sections:
        if section_name in article_dict['sections']:
            content = article_dict['sections'][section_name]
            lines = content.split('\n')
            if lines:
                # Take first non-empty line as title
                for line in lines:
                    if line.strip():
                        return line.strip()
    
    # If no title found in sections, try original filename
    if article_dict['original_filename']:
        # Clean up the filename to create a title
        clean_filename = article_dict['original_filename'].replace('.html', '')
        # Replace hyphens with spaces and capitalize words
        words = clean_filename.split('-')
        title = ' '.join(word.capitalize() for word in words)
        return title
    
    # If no original filename, use the markdown filename
    clean_filename = filename.replace('.md', '')
    words = clean_filename.split('-')
    title = ' '.join(word.capitalize() for word in words)
    return title

# Function 5: Extract Date
def extract_date(text):
    """
    Extract date from text and standardize to YYYY-MM-DD format.
    """
    # Various date patterns
    date_patterns = [
        r'(\d{1,2})\.(\d{1,2})\.(\d{4})',  # DD.MM.YYYY (German)
        r'(\d{1,2})[/\.](\d{1,2})[/\.](\d{4})',  # DD/MM/YYYY or MM/DD/YYYY
        r'(\d{4})-(\d{1,2})-(\d{1,2})',  # YYYY-MM-DD
        r'(\d{1,2})(?:st|nd|rd|th)? (?:of )?([A-Za-z]+)[,]? (\d{4})'  # 13th July 2021
    ]
    
    months = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04',
        'may': '05', 'june': '06', 'july': '07', 'august': '08',
        'september': '09', 'october': '10', 'november': '11', 'december': '12',
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'jun': '06',
        'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12',
        # German months
        'januar': '01', 'februar': '02', 'märz': '03', 'april': '04',
        'mai': '05', 'juni': '06', 'juli': '07', 'august': '08',
        'september': '09', 'oktober': '10', 'november': '11', 'dezember': '12'
    }
    
    for pattern in date_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            if len(match.groups()) == 3:
                if pattern == r'(\d{4})-(\d{1,2})-(\d{1,2})':  # YYYY-MM-DD
                    year, month, day = match.groups()
                elif pattern == r'(\d{1,2})(?:st|nd|rd|th)? (?:of )?([A-Za-z]+)[,]? (\d{4})':  # 13th July 2021
                    day, month_name, year = match.groups()
                    month = months.get(month_name.lower(), '01')
                else:  # DD.MM.YYYY or similar
                    day, month, year = match.groups()
                
                # Format as YYYY-MM-DD
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    
    # Look for month year formats (e.g., "Oktober 2015", "July 2021")
    month_year_pattern = r'([A-Za-z]+)\s+(\d{4})'
    month_year_match = re.search(month_year_pattern, text, re.IGNORECASE)
    if month_year_match:
        month_name, year = month_year_match.groups()
        month = months.get(month_name.lower(), '01')
        return f"{year}-{month}-01"
    
    # If there's a 4-digit year mentioned anywhere
    year_only = re.search(r'\b(20\d{2})\b', text)
    if year_only:
        return f"{year_only.group(1)}-01-01"
    
    # No date found, return empty string
    return ""

# Function 6: Extract Source
def extract_source(article_dict, text, language):
    """
    Extract the source of the article.
    Keep in original language.
    """
    # Check in Reference section
    reference_sections = ["Reference", "Referenz", "Quelle", "Source"]
    for section in reference_sections:
        if section in article_dict['sections']:
            source_text = article_dict['sections'][section]
            if source_text.strip():
                return source_text.strip()
    
    # Look for specific source patterns in the text
    source_patterns = [
        r'(?:Source|Quelle):\s*([^\.]+)',
        r'(?:By|Von|Author|Autor):\s*([^\.]+)',
        r'(?:Copyright|©)\s*([^\.]+)',
        r'(?:Published by|Veröffentlicht von):\s*([^\.]+)'
    ]
    
    for pattern in source_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    # Check for ETH departments or units
    eth_units = [
        r'(ETH[\s-]Zürich[^\.;,]*(?:Kommunikation|Communication|Department|Departement|Abteilung)[^\.;,]*)',
        r'(ETH[\s-]Zurich[^\.;,]*(?:Communication|Department|Unit|Division)[^\.;,]*)',
        r'((?:Hochschulkommunikation|University Communication)[^\.;,]*ETH[^\.;,]*)'
    ]
    
    for pattern in eth_units:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    # Extract potential domains from the filename
    if article_dict['original_filename']:
        domain_match = re.search(r'(?:www\.)?([a-z0-9-]+)\.(?:com|org|edu|ch|de)', article_dict['original_filename'], re.IGNORECASE)
        if domain_match:
            domain = domain_match.group(1).lower()
            if 'ethz' in domain:
                return "ETH Zürich" if language == "de" else "ETH Zurich"
            elif 'uzh' in domain:
                return "Universität Zürich" if language == "de" else "University of Zurich"
            else:
                # Format domain as a source
                domain = domain.replace('-', ' ').title()
                return domain
    
    # Default source based on language and content clues
    if "ETH" in text:
        return "ETH Zürich, Hochschulkommunikation" if language == "de" else "ETH Zurich, University Communications"
    
    # Generic fallback
    return "Unbekannte Quelle" if language == "de" else "Unknown source"

# Function 7: Extract Main Content
def extract_main_content(article_dict):
    """
    Extract the main content of the article.
    Keep in original language.
    """
    # Skip these sections
    skip_sections = ["Reference", "Referenz", "Quelle", "Source"]
    
    # If there's only one section and it's not in skip_sections, return it
    if len(article_dict['sections']) == 1:
        section_name = list(article_dict['sections'].keys())[0]
        if section_name not in skip_sections:
            return article_dict['sections'][section_name]
    
    # Combine all relevant sections
    content_parts = []
    
    for section_name, content in article_dict['sections'].items():
        if section_name not in skip_sections and content.strip():
            # Add section name as header if multiple sections
            if len(article_dict['sections']) > 1:
                content_parts.append(f"{section_name}: {content}")
            else:
                content_parts.append(content)
    
    # Join with double newlines to separate sections
    return "\n\n".join(content_parts)

# Function 8: Extract Named Entities
def extract_named_entities(text, language):
    """
    Extract named entities from text.
    Keep in original language.
    """
    if not text:
        return []
    
    # Normalize text for better extraction
    normalized_text = text.replace('\n', ' ').replace('  ', ' ')
    
    entities = []
    
    # First look for multi-word capitalized phrases (potential organizations and people)
    # This regex looks for 2-4 capitalized words in sequence
    org_pattern = r'\b([A-Z][a-zäöüÄÖÜß]+(?:[ \-][A-Z][a-zäöüÄÖÜß]+){1,3})\b'
    org_matches = re.findall(org_pattern, normalized_text)
    
    # Filter out common sentence starters and short phrases
    exclude_patterns = [
        r'^(?:The|A|An|Der|Die|Das|Ein|Eine|This|That|These|Those|Sie|Er|Es|Wir|Ich|Du)$',
        r'^[A-Za-z]{1,2}$'  # Exclude 1-2 letter entities
    ]
    
    for match in org_matches:
        if all(not re.match(pat, match) for pat in exclude_patterns) and len(match) > 3:
            entities.append(match)
    
    # Look for single-word organization names (typically capitalized nouns not at beginning of sentence)
    # This requires more filtering to avoid common words
    single_word_pattern = r'(?<![.!?]\s)\b([A-Z][a-zA-ZäöüÄÖÜß]{3,})\b'
    single_matches = re.findall(single_word_pattern, normalized_text)
    
    # Common words to exclude as entities
    common_words = set([
        "The", "This", "That", "These", "Those", "They", "Their", "And", "But", "However",
        "Der", "Die", "Das", "Diese", "Dieser", "Dieses", "Jene", "Und", "Aber", "Jedoch"
    ])
    
    for match in single_matches:
        if match not in common_words and not any(match in e for e in entities):
            entities.append(match)
    
    # ETH-specific named entities to look for
    eth_specific = []
    if language == "de":
        eth_specific = [
            "ETH Zürich", "ETH-Zürich", "ETH", "Universität Zürich", "UZH",
            "Hönggerberg", "ETH-Karte", "RFID-Chip", "ASVZ", "Polyterrasse"
        ]
    else:
        eth_specific = [
            "ETH Zurich", "ETH", "University of Zurich", "UZH",
            "Hönggerberg", "ETH Card", "RFID Chip", "ASVZ", "Polyterrasse"
        ]
    
    for entity in eth_specific:
        if entity in normalized_text and not any(entity in e for e in entities):
            entities.append(entity)
    
    # Look for people names mentioned with titles
    titles = ["Prof", "Professor", "Dr", "Professorin", "Doktor"]
    for title in titles:
        name_pattern = f"{title}\\.?\\s+([A-Z][a-zäöüÄÖÜß]+(?:\\s+[A-Z][a-zäöüÄÖÜß]+){{1,2}})"
        prof_matches = re.findall(name_pattern, normalized_text)
        entities.extend(prof_matches)
    
    # Deduplicate entities (case-insensitive)
    unique_entities = []
    seen = set()
    for entity in entities:
        if entity.lower() not in seen:
            seen.add(entity.lower())
            unique_entities.append(entity)
    
    # Return up to 10 entities
    return unique_entities[:10]

# Function 9: Extract Topics (Standardized to English)
def extract_topics(text, language):
    """
    Extract topics from text and standardize to English.
    """
    if not text:
        return ["University News"]
    
    # Pre-process text for better matching
    text_lower = text.lower()
    
    # Define comprehensive topic categories with weighted keyword sets
    # Format: (topic_name, [(keyword, weight), ...])
    topics_keywords = [
        ("Infrastructure", [
            ("karte", 3), ("card", 3), ("ausweis", 3), ("identification", 3),
            ("gebäude", 2), ("building", 2), ("raum", 1), ("room", 1),
            ("campus", 2), ("hönggerberg", 3), ("zentrum", 1), ("center", 1)
        ]),
        
        ("Technology & Innovation", [
            ("technologie", 3), ("technology", 3), ("innovation", 3), 
            ("digital", 2), ("software", 2), ("computer", 2), ("app", 2),
            ("rfid", 3), ("chip", 2), ("elektronisch", 1), ("electronic", 1),
            ("entwicklung", 1), ("development", 1), ("programmier", 2), ("coding", 2)
        ]),
        
        ("Research", [
            ("forschung", 3), ("research", 3), ("wissenschaft", 3), ("science", 3),
            ("studie", 2), ("study", 2), ("experiment", 2), ("projekt", 1), ("project", 1),
            ("entdeckung", 2), ("discovery", 2), ("publikation", 2), ("publication", 2)
        ]),
        
        ("Education", [
            ("ausbildung", 3), ("education", 3), ("studium", 3), ("studies", 3),
            ("student", 3), ("studierend", 3), ("lehre", 3), ("teaching", 3),
            ("vorlesung", 2), ("lecture", 2), ("kurs", 2), ("course", 2),
            ("prüfung", 2), ("exam", 2), ("seminar", 2), ("unterricht", 2)
        ]),
        
        ("Finance", [
            ("finanzen", 3), ("finance", 3), ("kosten", 3), ("costs", 3),
            ("preis", 3), ("price", 3), ("erhöhung", 2), ("increase", 2),
            ("budget", 3), ("geld", 2), ("money", 2), ("zahlung", 1), ("payment", 1)
        ]),
        
        ("University Administration", [
            ("verwaltung", 3), ("administration", 3), ("leitung", 2), ("management", 2),
            ("präsident", 2), ("president", 2), ("rektor", 2), ("rector", 2),
            ("direktor", 2), ("director", 2), ("strategie", 2), ("strategy", 2)
        ]),
        
        ("Campus Life", [
            ("campus", 3), ("student", 2), ("mensa", 3), ("cafeteria", 3),
            ("essen", 2), ("food", 2), ("veranstaltung", 2), ("event", 2),
            ("freizeit", 2), ("leisure", 2), ("sport", 2), ("asvz", 3)
        ]),
        
        ("International", [
            ("international", 3), ("global", 3), ("weltweit", 2), ("worldwide", 2),
            ("ausland", 2), ("foreign", 2), ("kooperation", 2), ("cooperation", 2),
            ("austausch", 2), ("exchange", 2), ("partner", 2)
        ]),
        
        ("Sustainability", [
            ("nachhaltig", 3), ("sustainable", 3), ("umwelt", 3), ("environment", 3),
            ("klima", 3), ("climate", 3), ("grün", 2), ("green", 2),
            ("energie", 2), ("energy", 2), ("ressource", 2), ("resource", 2)
        ]),
        
        ("Weather & Environment", [
            ("wetter", 3), ("weather", 3), ("sturm", 3), ("storm", 3),
            ("umwelt", 2), ("environment", 2), ("klima", 2), ("climate", 2),
            ("regen", 2), ("rain", 2), ("wind", 2), ("temperatur", 2), ("temperature", 2)
        ]),
        
        ("Communication", [
            ("kommunikation", 3), ("communication", 3), ("mitteilung", 3), ("announcement", 3),
            ("information", 2), ("bericht", 2), ("report", 2), ("news", 3),
            ("presse", 2), ("press", 2), ("media", 2), ("medien", 2)
        ]),
        
        ("Catering & Food", [
            ("mensa", 3), ("cafeteria", 3), ("essen", 3), ("food", 3),
            ("verpflegung", 3), ("catering", 3), ("restaurant", 2),
            ("speise", 2), ("meal", 2), ("menü", 2), ("menu", 2)
        ]),
        
        ("Staff", [
            ("mitarbeiter", 3), ("staff", 3), ("personal", 3), ("employee", 3),
            ("anstellung", 2), ("employment", 2), ("arbeit", 2), ("work", 2),
            ("position", 2), ("stelle", 2), ("job", 2)
        ]),
        
        ("COVID-19", [
            ("covid", 3), ("corona", 3), ("pandemic", 3), ("pandemie", 3),
            ("lockdown", 3), ("virus", 2), ("impfung", 2), ("vaccination", 2),
            ("maske", 2), ("mask", 2), ("abstand", 2), ("distance", 2)
        ])
    ]
    
    # Calculate scores for each topic
    topic_scores = {}
    
    for topic_name, keywords in topics_keywords:
        score = 0
        for keyword, weight in keywords:
            # Count occurrences of the keyword
            count = text_lower.count(keyword)
            if count > 0:
                score += count * weight
        
        if score > 0:
            topic_scores[topic_name] = score
    
    # If no topics found, add a default
    if not topic_scores:
        return ["University News"]
    
    # Sort topics by score and return top 6
    sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
    return [topic for topic, score in sorted_topics[:6]]

# Function 10: Extract Keywords (Standardized to English)
def extract_keywords(text, language):
    """
    Extract keywords from text and standardize to English.
    """
    if not text:
        return ["ETH Zurich"]
    
    # Normalize and lowercase text
    text_normalized = text.lower()
    
    # Define keyword mapping from German to English
    de_to_en = {
        "eth zürich": "ETH Zurich",
        "eth-karte": "ETH Card",
        "karte": "Card",
        "ausweis": "Identification Card",
        "studierende": "Students",
        "studenten": "Students",
        "student": "Student",
        "mitarbeitende": "Staff",
        "mitarbeiter": "Staff",
        "personal": "Personnel",
        "design": "Design",
        "erscheinungsbild": "Visual Identity",
        "forschung": "Research",
        "wissenschaft": "Science",
        "preiserhöhung": "Price Increase",
        "kosten": "Costs",
        "mensa": "Cafeteria",
        "verpflegung": "Catering",
        "unwetter": "Storm",
        "sturm": "Storm",
        "wetter": "Weather",
        "nachhaltigkeit": "Sustainability",
        "umwelt": "Environment",
        "klima": "Climate",
        "gebäude": "Building",
        "campus": "Campus",
        "hönggerberg": "Hönggerberg",
        "zentrum": "Campus Center",
        "technologie": "Technology",
        "innovation": "Innovation",
        "digital": "Digital",
        "lehre": "Teaching",
        "bildung": "Education",
        "kommunikation": "Communication"
    }
    
    # Initialize keywords list
    keywords = []
    
    # First check for specific multi-word terms
    if language == "de":
        # German multi-word terms with their English translations
        multi_word_de = {
            "eth zürich": "ETH Zurich",
            "eth-karte": "ETH Card",
            "elektronische karte": "Electronic ID",
            "corporate design": "Corporate Design",
            "neue design": "New Design",
            "universität zürich": "University of Zurich",
            "hönggerberg campus": "Hönggerberg Campus"
        }
        
        for de_term, en_term in multi_word_de.items():
            if de_term in text_normalized and en_term not in keywords:
                keywords.append(en_term)
    else:
        # English multi-word terms
        multi_word_en = [
            "ETH Zurich", "ETH Card", "Electronic ID", "Corporate Design",
            "New Design", "University of Zurich", "Hönggerberg Campus"
        ]
        
        for term in multi_word_en:
            if term.lower() in text_normalized and term not in keywords:
                keywords.append(term)
    
    # Check for single words and translate if German
    # First tokenize by removing punctuation and splitting
    translator = str.maketrans('', '', string.punctuation)
    words = text_normalized.translate(translator).split()
    
    # Get word frequency
    word_freq = {}
    for word in words:
        if len(word) > 3:  # Skip very short words
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Get the most frequent words
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Add top words, translating from German if needed
    for word, _ in sorted_words[:15]:  # Get top 15 words to ensure we have enough after filtering
        if language == "de" and word in de_to_en:
            en_word = de_to_en[word]
            if en_word not in keywords:
                keywords.append(en_word)
        elif language == "en" and len(word) > 3:
            # Capitalize the first letter for English words
            word_cap = word.capitalize()
            if word_cap not in keywords:
                keywords.append(word_cap)
    
    # Add specific ETH-related keywords if they're relevant
    eth_keywords = ["ETH Zurich", "University", "Research", "Science", "Campus", "Education"]
    for keyword in eth_keywords:
        if keyword not in keywords:
            keywords.append(keyword)
    
    # Return up to 7 keywords (deduped)
    unique_keywords = []
    seen = set()
    for kw in keywords:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            unique_keywords.append(kw)
    
    return unique_keywords[:7]

# Function to generate a summary
def generate_summary(text, max_length=200):
    """
    Generate a summary of the text.
    Keep in original language.
    """
    if not text:
        return ""
    
    # Take the first few sentences, up to max_length
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    summary = ""
    for sentence in sentences:
        if len(summary) + len(sentence) <= max_length:
            summary += sentence + " "
        else:
            break
    
    summary = summary.strip()
    
    # Add ellipsis if truncated
    if len(summary) < len(text) and summary:
        summary += "..."
    
    return summary

# Function 11: Generate Rich Metadata (Standardized to English)
def generate_rich_metadata(text, language):
    """
    Generate rich metadata for the article with standardized English fields.
    """
    if not text:
        return {
            "document_length_words": 0,
            "readability_score": "unknown",
            "sentiment": "neutral",
            "contains_compound_words": False,
            "contains_umlauts": False,
            "embedding_vector": "[...]",
            "audience_type": ["Students", "Staff"],
            "context_tags": ["ETH Internal"]
        }
    
    # Count words
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    # Determine readability (standardized to English)
    # More accurate approach based on sentence length and word length
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    avg_words_per_sentence = word_count / max(sentence_count, 1)
    long_words = len([w for w in words if len(w) > 6])
    long_word_percentage = (long_words / max(word_count, 1)) * 100
    
    if avg_words_per_sentence > 25 or long_word_percentage > 30:
        readability = "complex"
    elif avg_words_per_sentence > 15 or long_word_percentage > 20:
        readability = "moderately complex"
    else:
        readability = "easy to read"
    
    # Improved sentiment analysis with more keywords
    positive_patterns = [
        r'\b(?:gut|besser|positiv|erfolgreich|vorteil|nutzen|förder|erfreut|freude|verbessert)',
        r'\b(?:good|better|positive|successful|advantage|benefit|promote|pleased|improve|happy)'
    ]
    
    negative_patterns = [
        r'\b(?:schlecht|problem|negativ|schwierig|nachteil|kritisch|belastung|sorge|verschlechter)',
        r'\b(?:bad|problem|negative|difficult|disadvantage|critical|burden|worry|worsen)'
    ]
    
    positive_count = 0
    for pattern in positive_patterns:
        positive_count += len(re.findall(pattern, text.lower()))
    
    negative_count = 0
    for pattern in negative_patterns:
        negative_count += len(re.findall(pattern, text.lower()))
    
    # Calculate sentiment ratio
    total = positive_count + negative_count
    if total == 0:
        sentiment = "neutral"
    elif positive_count > negative_count * 2:
        sentiment = "positive"
    elif negative_count > positive_count * 2:
        sentiment = "negative"
    elif positive_count > negative_count:
        sentiment = "slightly positive"
    elif negative_count > positive_count:
        sentiment = "slightly negative"
    else:
        sentiment = "neutral"
    
    # Check for compound words and umlauts
    contains_compound_words = bool(re.search(r'\b\w{15,}\b', text))
    contains_umlauts = bool(re.search(r'[äöüÄÖÜß]', text))
    
    # Determine audience type (standardized to English)
    audience_type = []
    
    # More specific patterns for different audience types
    audience_patterns = [
        ("Students", [r'\bstud(?:ent|ierend|ium|ies)', r'\bschule\b', r'\buniversity\b']),
        ("Staff", [r'\bmitarbeit|\bpersonal|\bstaff|\bemployee|\bangestellt']),
        ("Faculty", [r'\bprofessor|\bdozent|\bfaculty|\blectur|\bdocent']),
        ("Researchers", [r'\bforsch|\bresearch|\bwissenschaft|\bscience|\blabor|\blab\b']),
        ("Administration", [r'\bverwaltung|\badministration|\bleitung|\bmanagement']),
        ("General Public", [r'\böffentlich|\bpublic|\ballgemein|\bgeneral|\bcommunity|\bgesellschaft'])
    ]
    
    for audience, patterns in audience_patterns:
        for pattern in patterns:
            if re.search(pattern, text.lower()):
                audience_type.append(audience)
                break
    
    # Default audience if none detected
    if not audience_type:
        audience_type = ["Students", "Staff"]
    
    # Context tags (standardized to English)
    context_tags = []
    
    # More comprehensive context tagging system
    context_patterns = [
        ("Financial", [r'\bfinan|\bkosten|\bbudget|\bcost|\bprice|\bpreis|\bgeld|\bmoney']),
        ("Catering", [r'\bmensa|\bessen|\bverpfleg|\bfood|\bdining|\bcafeteria|\bmahlzeit|\bmeal']),
        ("COVID-19", [r'\bcorona|\bcovid|\bpandemie|\bpandemic|\blockdown|\bvirus']),
        ("Sustainability", [r'\bnachhaltig|\bsustainable|\benvironment|\bumwelt|\bklima|\bclimate']),
        ("Infrastructure", [r'\bgebäude|\bbuilding|\binfrastruktur|\bcampus|\braum|\bspace']),
        ("Technology", [r'\btechnologie|\btechnology|\bdigital|\bsoftware|\brfid|\bapp']),
        ("Research", [r'\bforschung|\bresearch|\bwissenschaft|\bscience|\bstudie|\bstudy']),
        ("Education", [r'\bausbildung|\beducation|\bstudium|\bstudies|\blehre|\bteaching']),
        ("Administrative", [r'\bverwaltung|\badministration|\bmanagement|\bleitung|\bpolicy']),
        ("Communications", [r'\bkommunikation|\bcommunication|\bmitteilung|\bannouncement']),
        ("Events", [r'\bveranstaltung|\bevent|\bkonferenz|\bconference|\bmeeting|\bseminar']),
        ("Weather", [r'\bwetter|\bweather|\bsturm|\bstorm|\bregen|\brain|\btemperatur']),
        ("International", [r'\binternational|\bglobal|\bweltweit|\bworldwide|\bausland']),
        ("Career", [r'\bkarriere|\bcareer|\bjob|\bstelle|\bposition|\bbewerbung|\bapplication'])
    ]
    
    # Check for context tags
    for tag, patterns in context_patterns:
        for pattern in patterns:
            if re.search(pattern, text.lower()):
                context_tags.append(tag)
                break
    
    # Check if ETH-related
    if re.search(r'\beth|\bethz|\beidgenössische|\bpoly', text.lower()):
        context_tags.append("ETH Internal")
    
    # Limit to most relevant tags (max 4)
    if len(context_tags) > 4:
        context_tags = context_tags[:4]
    elif not context_tags:
        context_tags = ["University News"]
    
    # Create rich metadata with all fields in English
    rich_metadata = {
        "document_length_words": word_count,
        "readability_score": readability,
        "sentiment": sentiment,
        "contains_compound_words": contains_compound_words,
        "contains_umlauts": contains_umlauts,
        "embedding_vector": "[...]",
        "audience_type": audience_type,
        "context_tags": context_tags
    }
    
    return rich_metadata

# Main article processing function
def process_article(markdown_text, filename):
    """
    Process a single article through all cleaning steps.
    """
    try:
        # Step a: Basic cleaning
        cleaned_text = basic_text_cleaning(markdown_text)
        
        # Step b: Extract article structure
        article_structure = extract_article_structure(cleaned_text)
        
        # Step c: Extract main content (keep in original language)
        main_content = extract_main_content(article_structure)
        
        # Step d: Detect language
        language = detect_language(main_content or cleaned_text)
        
        # Step e: Extract title (keep in original language)
        title = extract_title(article_structure, filename)
        
        # Step f: Extract date (standardized format)
        date = extract_date(main_content or cleaned_text)
        
        # Step g: Extract source (keep in original language)
        source = extract_source(article_structure, main_content or cleaned_text, language)
        
        # Step h: Extract named entities (keep in original language)
        named_entities = extract_named_entities(main_content, language)
        
        # Step i: Extract topics (standardized to English)
        topics = extract_topics(main_content, language)
        
        # Step j: Extract keywords (standardized to English)
        keywords = extract_keywords(main_content, language)
        
        # Step k: Generate summary (keep in original language)
        summary = generate_summary(main_content)
        
        # Step l: Generate rich metadata (standardized to English)
        rich_metadata = generate_rich_metadata(main_content, language)
        
        # Create final structured document
        processed_article = {
            "language": language,
            "title": title,
            "date": date,
            "source": source,
            "main_content": main_content,
            "named_entities": named_entities,
            "topics": topics,
            "keywords": keywords,
            "summary": summary,
            "rich_metadata": rich_metadata
        }
        
        return processed_article
    
    except Exception as e:
        logger.error(f"Error processing {filename}: {str(e)}")
        # Return a minimal valid structure in case of failure
        return {
            "language": "unknown",
            "title": filename.replace('.md', '').replace('-', ' ').title(),
            "date": "",
            "source": "ETH Zurich",
            "main_content": "",
            "named_entities": [],
            "topics": ["University News"],
            "keywords": ["ETH Zurich"],
            "summary": "",
            "rich_metadata": {
                "document_length_words": 0,
                "readability_score": "unknown",
                "sentiment": "neutral",
                "contains_compound_words": False,
                "contains_umlauts": False,
                "embedding_vector": "[...]",
                "audience_type": ["Students", "Staff"],
                "context_tags": ["ETH Internal"]
            }
        }
