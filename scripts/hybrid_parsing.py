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
    structured_content = []  # To preserve structure with headings
    
    # Current section tracking
    current_section = {"title": "Main article", "content": []}

    # Keywords to identify sections to skip
    footer_keywords = ['newsletter', 'staffnet', 'globe', 'kontakt', 'contact']
    # Keywords that might appear in link text but shouldn't cause paragraph filtering
    allowed_link_keywords = ['download', 'pdf', 'here', 'hier']

    for section in sections:
        # Check if this is a footer/sidebar section to skip entirely
        h2 = section.find('h2')
        if h2 and any(kw in h2.get_text().lower() for kw in footer_keywords):
            logger.debug(f"Skipping section with title: {h2.get_text()}")
            continue
            
        # Preserve figcaption if it exists
        for fig in section.find_all('figure'):
            figcaption = fig.find('figcaption')
            if figcaption:
                caption_text = figcaption.get_text(" ", strip=True)
                if caption_text:
                    all_paragraphs.append(caption_text)
                    current_section["content"].append(caption_text)
            fig.decompose()

        # New section if h2 exists
        if h2:
            # Save previous section if it has content
            if current_section["content"]:
                structured_content.append(current_section)
                
            # Start a new section
            title_text = h2.get_text(strip=True)
            all_titles.append(title_text)
            current_section = {"title": title_text, "content": []}
        elif not all_titles and not structured_content:
            # If no h2 and no titles yet, add "Main article" title for first content
            all_titles.append("Main article")

        # Process unordered lists (bullet points)
        for ul in section.find_all('ul'):
            # Keep track if we've added the previous paragraph's context
            has_context = False
            
            # Get the previous paragraph for context if exists
            prev_p = ul.find_previous('p')
            prev_text = ""
            if prev_p:
                prev_text = prev_p.get_text(" ", strip=True)
                if prev_text and prev_text.endswith(':'):
                    # This is likely a list header, add it as context
                    all_paragraphs.append(prev_text)
                    current_section["content"].append(prev_text)
                    has_context = True
            
            # Process list items
            li_paragraphs = []
            for li in ul.find_all('li'):
                li_text = li.get_text(" ", strip=True)
                if li_text:
                    # Format as bullet points
                    li_text = f"• {li_text}"
                    li_paragraphs.append(li_text)
            
            # If we have list items, add them
            if li_paragraphs:
                if not has_context and prev_text and not prev_text.endswith('.'):
                    # If previous paragraph doesn't end with period,
                    # it might be context for the list even if not ending with ':'
                    all_paragraphs.append(prev_text)
                    current_section["content"].append(prev_text)
                
                # Add list items
                all_paragraphs.extend(li_paragraphs)
                current_section["content"].extend(li_paragraphs)

        #  Extract paragraphs (that aren't part of lists)
        for p in section.find_all('p'):
            # Skip if this paragraph is attached to a list and already processed
            next_sibling = p.find_next_sibling()
            if next_sibling and next_sibling.name == 'ul':
                # If para ends with colon, it's likely a list intro
                text = p.get_text(" ", strip=True)
                if text and text.endswith(':'):
                    continue
            
            # Get original HTML to detect if it contains downloads we want to preserve
            p_html = str(p)
            has_important_links = any(kw in p_html.lower() for kw in allowed_link_keywords)
            
            # Get clean text
            text = p.get_text(" ", strip=True)
            
            # Clean up link artifacts
            text = text.replace("external page", "").replace("call_made", "")
            text = text.replace("vertical_align_bottom", "").replace("Download", "")
            text = ' '.join(text.split())  # Normalize extra spaces
            
            if not text:
                continue
                
            # Skip short texts unless they contain important links
            if len(text) < 20 and not has_important_links:
                continue
                
            # Only filter by footer keywords if not an important link
            if not has_important_links and any(kw in text.lower() for kw in footer_keywords):
                continue
                
            all_paragraphs.append(text)
            current_section["content"].append(text)
    
    # Add the last section if it has content
    if current_section["content"]:
        structured_content.append(current_section)
    
    # If we didn't find any content, try a less strict approach
    if not all_paragraphs:
        logger.warning("No paragraphs found with standard method, trying fallback approach")
        # Try to get all paragraphs and lists
        for p in soup.find_all('p'):
            text = p.get_text(" ", strip=True)
            if text and len(text) > 20:
                all_paragraphs.append(text)
                
        # Try to get lists in fallback mode too
        for ul in soup.find_all('ul'):
            for li in ul.find_all('li'):
                li_text = li.get_text(" ", strip=True)
                if li_text:
                    all_paragraphs.append(f"• {li_text}")
    
    return {
        'titles': all_titles,
        'body': '<br><br>'.join(all_paragraphs),  # use <br><br> for clearer formatting
        'paragraphs': all_paragraphs,
        'structured_content': structured_content
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
    # Read the HTML file with error handling for different encodings
    encodings_to_try = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    html_content = None
    
    for encoding in encodings_to_try:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                html_content = f.read()
                logger.debug(f"Successfully read file with {encoding} encoding")
                break
        except UnicodeDecodeError:
            logger.debug(f"Failed to read with {encoding} encoding, trying next...")
    
    if html_content is None:
        raise ValueError(f"Could not read file with any encoding: {filepath}")

    
    # Use BeautifulSoup to extract clean body and titles
    bs4_data = parse_with_bs4(html_content)
    
    # Use Docling to extract structured markdown
    try:
        docling_data = parse_with_docling(str(filepath))
    except Exception as e:
        logger.warning(f"Docling parsing failed: {e}. Using fallback.")
        docling_data = {'body': '## Main article\n\n'}
    
    
    # Merge structured_content from bs4_data
    structured_content = bs4_data.get('structured_content', [])
    
    return {
        'filepath': filepath,
        'filename': filepath.name,
        'bs4_body': bs4_data['body'],
        'bs4_titles': bs4_data['titles'],
        'bs4_paragraphs': bs4_data['paragraphs'],
        'structured_content': structured_content,
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
    
    # Check if we extracted any content
    if not result['bs4_paragraphs']:
        logger.warning(f"No content extracted from {html_file}")
        if dry_run:
            return {
                'html_file': html_file,
                'markdown_file': None,
                'chunks': [],
                'status': 'empty'
            }
    
    # Create markdown content
    markdown_content = f"# {html_file.stem}\n\n"
    
    # Add metadata section
    markdown_content += f"**Source:** {html_file.relative_to(html_file.parents[3])}\n\n"
    markdown_content += f"**Date processed:** {pd.Timestamp.now().strftime('%Y-%m-%d')}\n\n"
    
    # Use the structured content if available
    if 'structured_content' in result and result['structured_content']:
        for section in result['structured_content']:
            markdown_content += f"## {section['title']}\n\n"
            
            for paragraph in section['content']:
                clean = paragraph.strip()
                if clean:
                    # Preserve bullet points formatting
                    if clean.startswith('• '):
                        markdown_content += clean + "\n"
                    else:
                        markdown_content += clean + "\n\n"
    else:
        # Fallback to the old method
        # Create chunks
        docling_chunks = chunk_docling_markdown(result['docling_markdown'])
        content_chunks = distribute_bs4_text(result['bs4_paragraphs'], docling_chunks)
        
        # Inject bullet points into the first chunk's body (only if needed)
        if content_chunks:
            content_chunks[0]["body"] = inject_docling_bullets(
                bs4_body=content_chunks[0]["body"],
                docling_markdown=result['docling_markdown']
            )
            
        # Add content chunks
        for chunk in content_chunks:
            markdown_content += f"## {chunk['title']}\n\n"
            paragraphs = chunk['body'].split('<br><br>')
            for p in paragraphs:
                clean = p.strip()
                if clean:
                    # Preserve bullet points formatting
                    if clean.startswith('• '):
                        markdown_content += clean + "\n"
                    else:
                        markdown_content += clean + "\n\n"
    
    # Define the output file path - keep the same structure as the original
    markdown_file = html_file.with_suffix('.md')
    
    if not dry_run:
        # Create parent directories if they don't exist
        markdown_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Make sure we have some content before saving
        if len(''.join(result['bs4_paragraphs'])) > 30:
            # Save the markdown file
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logger.info(f"Saved: {markdown_file}")
        else:
            logger.warning(f"Skipped saving {markdown_file} - insufficient content")
    else:
        logger.info(f"Would save to: {markdown_file}")
        
        # Debug output for dry run to check content
        logger.debug(f"Content preview:\n{markdown_content[:500]}...")
    
    return {
        'html_file': html_file,
        'markdown_file': markdown_file,
        'content': markdown_content,
        'status': 'success'
    }

def main():
    """
    Main function to process HTML files
    """
    parser = argparse.ArgumentParser(description='Hybrid HTML Parser using BeautifulSoup + Docling')
    parser.add_argument('--root', type=str, default='HKNews', help='Root directory to search for HTML files')
    parser.add_argument('--output', type=str, default=None, help='Output directory (default: same as input)')
    parser.add_argument('--dry-run', action='store_true', help='Don\'t save files, just simulate')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('--file', type=str, default=None, help='Process a single file instead of entire directory')
    parser.add_argument('--summary', action='store_true', help='Generate summary report')
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Convert root to Path object
    root_dir = Path(args.root)
    
    # Find files to process
    if args.file:
        # Process single file
        file_path = Path(args.file)
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return
        html_files = [file_path]
    else:
        # Find all HTML files in directory
        html_files = find_html_files(root_dir)
    
    logger.info(f"Found {len(html_files)} HTML files to process")
    
    # Process each file
    processed_files = []
    errors = []
    empty_files = []
    
    for html_file in html_files:
        try:
            result = process_html_file(html_file, dry_run=args.dry_run)
            processed_files.append(result)
            
            # Track empty files
            if result.get('status') == 'empty':
                empty_files.append(html_file)
                
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
            errors.append((html_file, str(e)))
    
    # Generate processing report
    success_count = len(processed_files) - len(empty_files) - len(errors)
    logger.info(f"Processing complete:")
    logger.info(f"  - Successfully processed: {success_count} files")
    logger.info(f"  - Empty content (skipped): {len(empty_files)} files")
    logger.info(f"  - Errors: {len(errors)} files")
    
    # Generate detailed summary report if requested
    if args.summary and not args.dry_run:
        summary_file = root_dir / "parsing_summary.txt"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# HTML Parsing Summary Report\n")
            f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total files processed: {len(html_files)}\n")
            f.write(f"Successfully processed: {success_count}\n")
            f.write(f"Empty content (skipped): {len(empty_files)}\n")
            f.write(f"Errors: {len(errors)}\n\n")
            
            if empty_files:
                f.write("## Files with empty content\n")
                for file in empty_files:
                    f.write(f"- {file.relative_to(root_dir)}\n")
                f.write("\n")
            
            if errors:
                f.write("## Files with errors\n")
                for file, error in errors:
                    f.write(f"- {file.relative_to(root_dir)}: {error}\n")
                    
        logger.info(f"Summary report saved to {summary_file}")

if __name__ == "__main__":
    main()