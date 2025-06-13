import os
import sqlite3
import shutil
from pathlib import Path

def fix_chromadb():
    """Complete ChromaDB reassembly including embeddings"""
    
    parts_dir = Path('chromadb_parts')
    output_dir = Path('notebooks/chroma_db_fixed')
    
    # Step 1: Get the collection UUID mappings
    conn = sqlite3.connect(output_dir / 'chroma.sqlite3')
    cursor = conn.cursor()
    
    # Get all segment IDs
    cursor.execute("""
        SELECT s.id, c.name, s.type, s.scope
        FROM segments s
        JOIN collections c ON s.collection_id = c.id
        WHERE c.name = 'news_multilingual_recursive'
    """)
    
    segments = cursor.fetchall()
    print(f"Found {len(segments)} segments for news_multilingual_recursive")
    
    # Find the vector segment (HNSW index)
    vector_segment_id = None
    for seg_id, col_name, seg_type, seg_scope in segments:
        print(f"  Segment: {seg_id}, Type: {seg_type}, Scope: {seg_scope}")
        if seg_type == 'urn:chroma:segment/vector/hnsw':
            vector_segment_id = seg_id
    
    if not vector_segment_id:
        print("ERROR: No vector segment found!")
        return
    
    print(f"\nVector segment ID: {vector_segment_id}")
    
    # Step 2: Create the segment directory and reassemble files
    segment_dir = output_dir / vector_segment_id
    segment_dir.mkdir(exist_ok=True)
    
    # Reassemble data_level0.bin
    print("\nReassembling data_level0.bin...")
    output_file = segment_dir / 'data_level0.bin'
    
    with open(output_file, 'wb') as outfile:
        for part in ['data_level0.bin_part_aa', 'data_level0.bin_part_ab', 'data_level0.bin_part_ac']:
            part_path = parts_dir / part
            if part_path.exists():
                print(f"  Reading {part}...")
                with open(part_path, 'rb') as infile:
                    outfile.write(infile.read())
            else:
                print(f"  WARNING: {part} not found!")
    
    print(f"  Created {output_file.name}: {output_file.stat().st_size:,} bytes")
    
    # Copy other HNSW index files
    print("\nCopying index metadata...")
    index_files = ['index_metadata.pickle', 'header.bin', 'length.bin', 'link_lists.bin']
    
    for filename in index_files:
        src = parts_dir / filename
        if src.exists():
            dst = segment_dir / filename
            shutil.copy2(src, dst)
            print(f"  Copied {filename}: {dst.stat().st_size:,} bytes")
        else:
            # These files might not exist in the parts
            print(f"  {filename} not found in parts (may not be needed)")
    
    # Step 3: Verify the collection has documents
    cursor.execute("""
        SELECT COUNT(*) FROM embeddings e
        JOIN segments s ON e.segment_id = s.id
        JOIN collections c ON s.collection_id = c.id
        WHERE c.name = 'news_multilingual_recursive'
    """)
    
    doc_count = cursor.fetchone()[0]
    print(f"\nDocuments in database: {doc_count}")
    
    conn.close()
    
    print("\nChromaDB reassembly complete!")
    print(f"Files in {segment_dir}:")
    for f in segment_dir.iterdir():
        print(f"  {f.name}: {f.stat().st_size:,} bytes")

if __name__ == "__main__":
    fix_chromadb()
