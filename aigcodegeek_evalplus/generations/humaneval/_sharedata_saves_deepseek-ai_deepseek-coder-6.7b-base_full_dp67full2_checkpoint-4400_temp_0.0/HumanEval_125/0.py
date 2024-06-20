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
    words = []
    if ' ' in txt:
        words = txt.split()
    elif ',' in txt:
        words = txt.split(',')
    else:
        odd_letters = sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)
        return odd_letters

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))