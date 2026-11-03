import json
from pathlib import Path

from src.preprocessing.text_chunker import chunk_pages

# Input and output paths
input_path = Path("data/processed/ir_syllabus_cleaned.json")
output_path = Path("data/processed/ir_syllabus_chunks.json")

# Read cleaned PDF data
with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)

# Divide text into smaller chunks
chunks = chunk_pages(pages, chunk_size=500, overlap=50)

# Save chunks as JSON
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=4, ensure_ascii=False)

print("Text chunking successful!")
print("Total chunks created:", len(chunks))
print("Chunk data saved to:", output_path)