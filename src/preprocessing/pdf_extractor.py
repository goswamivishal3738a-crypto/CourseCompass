
import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file page by page.

    Args:
        pdf_path: Path to the PDF document.

    Returns:
        A list containing the extracted text and page number.
    """

    extracted_pages = []

    # Open the PDF document
    document = fitz.open(pdf_path)

    # Read each page one by one
    for page_number, page in enumerate(document, start=1):

        # Extract text from the current page
        page_text = page.get_text("text")

        # Store non-empty pages with their page numbers
        if page_text.strip():
            extracted_pages.append({
                "page_number": page_number,
                "text": page_text
            })

    # Close the PDF document
    document.close()

    return extracted_pages
