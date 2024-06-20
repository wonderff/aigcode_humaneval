def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_with_unique_chars = [(word, len(set(word))) for word in words]
    max_unique_chars = max(words_with_unique_chars, key=lambda x: x[1])[1]
    max_words = [word for word, unique_chars in words_with_unique_chars if unique_chars == max_unique_chars]
    return min(max_words)

print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb", "cc"])) # "aaaaaaa"