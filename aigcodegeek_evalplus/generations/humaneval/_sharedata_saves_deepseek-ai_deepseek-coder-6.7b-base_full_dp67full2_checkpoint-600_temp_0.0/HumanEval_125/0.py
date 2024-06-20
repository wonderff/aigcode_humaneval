def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        lower_case_odd_order_count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 != 0)
        return lower_case_odd_order_count

# Test cases
print(split_words("Hello world!"))  # ["Hello", "world!"]
print(split_words("Hello,world!"))  # ["Hello", "world!"]
print(split_words("abcdef"))  # 3