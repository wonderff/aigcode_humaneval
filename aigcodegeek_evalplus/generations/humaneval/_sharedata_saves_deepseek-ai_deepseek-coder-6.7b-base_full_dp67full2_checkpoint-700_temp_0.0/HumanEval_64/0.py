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
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count(""))  # 0
print(vowels_count("Y"))  # 1
print(vowels_count("A"))  # 1
print(vowels_count("E"))  # 1
print(vowels_count("I"))  # 1
print(vowels_count("O"))  # 1
print(vowels_count("U"))  # 1
print(vowels_count("QX"))  # 0
print(vowels_count("PYTHON"))  # 2
print(vowels_count("Aa"))  # 1
print(vowels_count("Ee"))  # 1
print(vowels_count("Ii"))  # 1
print(vowels_count("Oo"))  # 1
print(vowels_count("Uu"))  # 1
print(vowels_count("Qx"))  # 0
print(vowels_count("PythoN"))  # 2