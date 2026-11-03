
import json
from pathlib import Path
from src.preprocessing.pdf_extractor import extract_text_from_pdf

# Define input and output paths
pdf_path = Path("data/raw/ir_syllabus.pdf")
output_path = Path("data/processed/ir_syllabus.json")

if not pdf_path.exists():
    print("Error: PDF not found!")

else:
    # Extract PDF text
    pages = extract_text_from_pdf(pdf_path)

    # Save extracted text as JSON
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(pages, file, indent=4, ensure_ascii=False)

    print("PDF extraction successful!")
    print("Pages extracted:", len(pages))
    print("Extracted text saved to:", output_path)
