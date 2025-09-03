def get_book_text(filepath):
    """Reads a text file and returns its contents as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
