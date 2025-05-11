import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_and_chunk(
    source_folder: str = "data", 
    chunk_size: int = 500, 
    chunk_overlap: int = 100
) -> list[str]:
    """
    Load all .txt files from a folder and split them into meaningful text chunks.

    Args:
        source_folder: Directory containing .txt documents.
        chunk_size: Maximum characters per chunk.
        chunk_overlap: Overlap between consecutive chunks to preserve context.

    Returns:
        List of text chunks.
    """
    # Find all text files in the source folder
    files = list(Path(source_folder).glob("*.txt"))
    if not files:
        raise FileNotFoundError(f"No .txt files found in {source_folder}")

    # Configure the text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )

    all_chunks = []
    for file in files:
        text = file.read_text(encoding="utf-8")
        # Split into chunks preserving meaningful boundaries
        chunks = splitter.split_text(text)
        all_chunks.extend(chunks)
    return all_chunks


if __name__ == "__main__":
    chunks = load_and_chunk()
    # Example output: print first 3 chunks
    for idx, chunk in enumerate(chunks, 1):
        print(f"--- Chunk {idx} ---")
        print(chunk)
