
import re


def clean_text(text):
    """
    Clean extracted syllabus text.

    Args:
        text: Raw text extracted from a PDF.

    Returns:
        Cleaned text.
    """

    # Replace multiple spaces and tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple line breaks with a single line break
    text = re.sub(r"\n+", "\n", text)

    # Remove spaces at the beginning and end
    text = text.strip()

    return text


def clean_extracted_pages(pages):
    """
    Clean text from all extracted PDF pages.

    Preserve page numbers and page structure.
    """

    cleaned_pages = []

    for page in pages:
        cleaned_text = clean_text(page["text"])

        cleaned_pages.append({
            "page_number": page["page_number"],
            "text": cleaned_text
        })

    return cleaned_pages
