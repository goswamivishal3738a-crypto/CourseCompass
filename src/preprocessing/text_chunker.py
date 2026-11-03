def chunk_text(text, chunk_size=500, overlap=50):
    """
    Divide text into smaller overlapping chunks.

    Args:
        text: Cleaned text.
        chunk_size: Maximum words in each chunk.
        overlap: Number of words shared between chunks.

    Returns:
        A list of text chunks.
    """

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_pages(pages, chunk_size=500, overlap=50):
    """
    Create chunks from all pages while preserving page numbers.
    """

    all_chunks = []

    for page in pages:

        page_chunks = chunk_text(
            page["text"],
            chunk_size,
            overlap
        )

        for chunk_number, chunk in enumerate(page_chunks, start=1):

            all_chunks.append({
                "page_number": page["page_number"],
                "chunk_number": chunk_number,
                "text": chunk
            })

    return all_chunks