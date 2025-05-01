#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hybrid HTML Parser using BeautifulSoup + Docling

Author: Daria
Goal: Extract and clean main text content from HTML news articles.
Implements a hybrid parsing strategy combining BeautifulSoup and Docling for robustness and quality.
"""

# Imports
from bs4 import BeautifulSoup
import pandas as pd
import os
import matplotlib.pyplot as plt
from docling.document_converter import DocumentConverter
import re
import argparse
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create a Docling converter
docling_converter = DocumentConverter()

def parse_with_bs4(html_content):
    """
    Parse HTML content using BeautifulSoup
    
    Args:
        html_content (str): HTML content as string
        
    Returns:
        dict: Dictionary containing titles, body text, and paragraphs
    """
    soup = BeautifulSoup(html_content, 'lxml')

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Identify main article sections
    sections = soup.find_all('div', class_='text-image cq-dd-image')
    
    all_titles = []
    all_paragraphs = []

    footer_keywords = ['newsletter', 'staffnet', 'globe', 'download']

    for section in sections:
        # Preserve figcaption if it exists
        for fig in section.find_all('figure'):
            # Preserve figcaption if it exists
            figcaption = fig.find('figcaption')
            if figcaption:
                caption_text = figcaption.get_text(" ", strip=True)
                if caption_text:
                    all_paragraphs.append(caption_text)
            fig.decompose()

        # Skip footer sections based on title
        h2 = section.find('h2')
        if h2:
            title_text = h2.get_text(strip=True)
            if any(kw in title_text.lower() for kw in footer_keywords):
                continue
            all_titles.append(title_text)
        else:
            # If no h2, add "Main article" title for first/main content
            if not all_titles:
                all_titles.append("Main article")

        #  Paragraph extraction
        for p in section.find_all('p'):
            text = p.get_text(" ", strip=True)

            # Clean up link artifacts like "external page", "call_made"
            text = text.replace("external page", "").replace("call_made", "")
            text = ' '.join(text.split())  # Normalize extra spaces
            
            if not text:
                continue
            if any(kw in text.lower() for kw in footer_keywords):
                continue
            if len(text) < 20:
                continue
            all_paragraphs.append(text)
            
    return {
        'titles': all_titles,
        'body': '<br><br>'.join(all_paragraphs),  # use <br><br> for clearer formatting
        'paragraphs': all_paragraphs
    }

def parse_with_docling(filepath):
    """
    Parse HTML file using Docling
    
    Args:
        filepath (str): Path to the HTML file
        
    Returns:
        dict: Dictionary containing body text in markdown format
    """
    result = docling_converter.convert(filepath)
    text = result.document.export_to_markdown()
    return {
        'body': text
    }

def inject_docling_bullets(bs4_body, docling_markdown):
    """
    Extract and inject bullet points from Docling markdown into BS4 body
    
    Args:
        bs4_body (str): Body text from BeautifulSoup
        docling_markdown (str): Markdown text from Docling
        
    Returns:
        str: Updated body text with bullet points
    """
    # Extract bullet-style lines from docling
    bullet_lines = [
        line.strip()
        for line in docling_markdown.splitlines()
        if line.strip().startswith(('•', '- '))
    ]

    logger.debug(f"Bullet lines extracted from Docling: {bullet_lines}")

    # Keep only bullets not already in bs4_body
    unique_bullets = [
        bullet for bullet in bullet_lines
        if bullet not in bs4_body
    ]

    if not unique_bullets:
        return bs4_body

    # Prepend them at the top with <br> spacing
    bullet_block = '<br><br>' + '<br><br>'.join(unique_bullets) + '<br><br>'
    return bullet_block + bs4_body

def hybrid_parser_from_file(filepath):
    """
    Hybrid parser that works directly with the file
    
    Args:
        filepath (Path): Path object to the HTML file
        
    Returns:
        dict: Dictionary containing parsed data from both parsers
    """
    # Read the HTML file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except UnicodeDecodeError:
        # Try with a different encoding if UTF-8 fails
        with open(filepath, 'r', encoding='latin-1') as f:
            html_content = f.read()
    
    # Use BeautifulSoup to extract clean body and titles
    bs4_data = parse_with_bs4(html_content)
    
    # Use Docling to extract structured markdown
    docling_data = parse_with_docling(str(filepath))

    return {
        'filepath': filepath,
        'filename': filepath.name,
        'bs4_body': bs4_data['body'],
        'bs4_titles': bs4_data['titles'],
        'bs4_paragraphs': bs4_data['paragraphs'],
        'docling_markdown': docling_data['body']
    }

def chunk_docling_markdown(markdown_text):
    """
    Split docling markdown into sections using ## headers.
    Fallback to one generic chunk if headers are missing or irrelevant.
    
    Args:
        markdown_text (str): Markdown text from Docling
        
    Returns:
        list: List of dictionaries containing title and text
    """
    chunks = []
    current = {"title": None, "text": ""}
    for line in markdown_text.splitlines():
        if line.startswith("## "):
            if current["title"] or current["text"].strip():
                chunks.append(current)
            current = {"title": line[3:].strip(), "text": ""}
        else:
            current["text"] += line + "\n"
    if current["title"] or current["text"].strip():
        chunks.append(current)

    # If only footers are present, ignore them and use a fallback chunk
    footer_keywords = ["staffnet", "newsletter", "kontakt", "about"]
    only_footers = all(any(kw in (c["title"] or "").lower() for kw in footer_keywords) for c in chunks)

    if len(chunks) < 2 or only_footers:
        return [{"title": "Main article", "text": ""}]
    else:
        return chunks

def distribute_bs4_text(paragraphs, docling_chunks):
    """
    Distribute list of BS4 paragraphs into Docling-defined chunks
    
    Args:
        paragraphs (list): List of paragraphs from BeautifulSoup
        docling_chunks (list): List of chunks from Docling
        
    Returns:
        list: Updated list of chunks with body text
    """
    n = len(docling_chunks)
    m = len(paragraphs)
    avg = max(1, m // n) if n > 0 else m

    for i, chunk in enumerate(docling_chunks):
        start = i * avg
        end = m if i == n - 1 else (i + 1) * avg
        chunk["body"] = "\n\n" + "\n\n".join(paragraphs[start:end])
    
    return docling_chunks

def find_html_files(root_dir):
    """
    Find all HTML files in the directory structure
    
    Args:
        root_dir (Path): Root directory to start the search
        
    Returns:
        list: List of Path objects for HTML files
    """
    html_files = []
    for path in root_dir.glob('**/*.html'):
        html_files.append(path)
    return html_files

def process_html_file(html_file, dry_run=False):
    """
    Process a single HTML file and save its markdown version
    
    Args:
        html_file (Path): Path to the HTML file
        dry_run (bool): If True, don't save files but just log actions
        
    Returns:
        dict: Dictionary containing processing results
    """
    logger.info(f"Processing: {html_file}")
    
    # Parse the file
    result = hybrid_parser_from_file(html_file)
    
    # Create chunks
    docling_chunks = chunk_docling_markdown(result['docling_markdown'])
    content_chunks = distribute_bs4_text(result['bs4_paragraphs'], docling_chunks)
    
    # Inject bullet points into the first chunk's body (only if needed)
    if content_chunks:
        content_chunks[0]["body"] = inject_docling_bullets(
            bs4_body=content_chunks[0]["body"],
            docling_markdown=result['docling_markdown']
        )
    
    # Create markdown content
    markdown_content = f"# {html_file.stem}\n\n"
    for chunk in content_chunks:
        markdown_content += f"## {chunk['title']}\n\n"
        paragraphs = chunk['body'].split('<br><br>')
        for p in paragraphs:
            clean = p.strip()
            if clean:
                markdown_content += clean + "\n\n"
    
    # Define the output file path
    markdown_file = html_file.with_suffix('.md')
    
    if not dry_run:
        # Create parent directories if they don't exist
        markdown_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Save the markdown file
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        logger.info(f"Saved: {markdown_file}")
    else:
        logger.info(f"Would save to: {markdown_file}")
    
    return {
        'html_file': html_file,
        'markdown_file': markdown_file,
        'chunks': content_chunks
    }

def main():
    """
    Main function to process HTML files
    """
    parser = argparse.ArgumentParser(description='Hybrid HTML Parser using BeautifulSoup + Docling')
    parser.add_argument('--root', type=str, default='HKNews', help='Root directory to search for HTML files')
    parser.add_argument('--dry-run', action='store_true', help='Don\'t save files, just simulate')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Convert root to Path object
    root_dir = Path(args.root)
    
    # Find all HTML files
    html_files = find_html_files(root_dir)
    logger.info(f"Found {len(html_files)} HTML files to process")
    
    # Process each file
    processed_files = []
    for html_file in html_files:
        try:
            result = process_html_file(html_file, dry_run=args.dry_run)
            processed_files.append(result)
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
    
    logger.info(f"Successfully processed {len(processed_files)} files")
    
    # Optional: Generate a summary report
    if processed_files:
        logger.info("Processing complete")

if __name__ == "__main__":
    main()
    