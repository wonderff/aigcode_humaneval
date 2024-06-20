FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiou"
    s = s.lower()
    count = sum(1 for char in s if char in vowels)
    if s[-1] == "y":
        count += 1
    return count

# Test cases
print(vowels_count("abcde")) # 2
print(vowels_count("ACEDY")) # 3
print(vowels_count("hello")) # 2
print(vowels_count("HELLO")) # 2
print(vowels_count("PYTHON")) # 3
print(vowels_count("PYTHONY")) # 4
print(vowels_count("")) # 0
print(vowels_count("Y")) # 1
print(vowels_count("AEIOU")) # 5
print(vowels_count("EDY")) # 3