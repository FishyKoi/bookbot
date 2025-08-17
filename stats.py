# stats.py

# Read the book file and return its contents as a string
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


# Count the number of words in the text
def get_num_words(text):
    return len(text.split())


# Count occurrences of each character in the text (case-insensitive)
def get_char_count(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


# Convert the character counts dictionary into a sorted list of dictionaries
# [{"char": "a", "num": 123}, ...] sorted from highest to lowest count
def sort_char_counts(char_dict):
    sorted_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
