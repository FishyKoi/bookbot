import sys
from stats import get_book_text, get_num_words, get_char_count, sort_char_counts

def main():
    # Check that the user passed exactly one argument for the book path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Get the path from the command-line arguments

    # Read the book
    book_text = get_book_text(book_path)

    # Count words
    num_words = get_num_words(book_text)

    # Count characters
    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_counts(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        # Only print alphabetical characters
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
