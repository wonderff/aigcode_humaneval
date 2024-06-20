def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_lowercase = [word.lower() for word in words]
    unique_chars = [len(set(word)) for word in words_lowercase]
    max_unique = max(unique_chars)
    max_unique_words = [word for idx, word in enumerate(words) if unique_chars[idx] == max_unique]
    return min(max_unique_words)