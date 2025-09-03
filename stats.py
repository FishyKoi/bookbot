def get_num_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def get_char_counts(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_dict):
    """Converts char counts dict into a sorted list of dicts."""
    char_list = []
    for char, num in char_dict.items():
        if char.isalpha():  # skip non-alphabet characters
            char_list.append({"char": char, "num": num})

    # sort in-place, greatest to least
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list
