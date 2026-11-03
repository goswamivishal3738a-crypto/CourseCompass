
import json
from pathlib import Path

from src.preprocessing.text_cleaner import clean_extracted_pages

# Input and output JSON paths
input_path = Path("data/processed/ir_syllabus.json")
output_path = Path("data/processed/ir_syllabus_cleaned.json")

# Read extracted PDF data
with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)

# Clean all extracted pages
cleaned_pages = clean_extracted_pages(pages)

# Save cleaned data
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(cleaned_pages, file, indent=4, ensure_ascii=False)

print("Text cleaning successful!")
print("Total pages cleaned:", len(cleaned_pages))
print("Cleaned data saved to:", output_path)
