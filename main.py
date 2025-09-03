import sys
from bookbot import get_book_text
from stats import get_num_words, get_char_counts, sort_char_counts

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # take the book path from the command-line
    book_text = get_book_text(filepath)

    # Word count
    num_words = get_num_words(book_text)

    # Character counts
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
