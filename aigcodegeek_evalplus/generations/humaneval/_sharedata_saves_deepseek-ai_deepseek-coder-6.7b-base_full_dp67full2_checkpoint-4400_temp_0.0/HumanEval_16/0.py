def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Create a set of characters to store the distinct characters
    distinct_characters = set(string)
    # Return the length of the set
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4