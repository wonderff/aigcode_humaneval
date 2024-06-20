def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    for char in string.lower():
        distinct_chars.add(char)
    
    return len(distinct_chars)

print(count_distinct_characters('xyzXYZ')) # 3
print(count_distinct_characters('Jerry')) # 4
print(count_distinct_characters('Hello')) # 4