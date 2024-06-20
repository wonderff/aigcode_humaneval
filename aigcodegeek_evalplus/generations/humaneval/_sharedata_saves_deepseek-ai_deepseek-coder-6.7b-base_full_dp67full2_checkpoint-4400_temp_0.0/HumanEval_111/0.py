def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    test = test.split()
    freq = {}
    max_freq = 0
    for letter in test:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
        max_freq = max(max_freq, freq[letter])
    
    result = {}
    for key in freq:
        if freq[key] == max_freq:
            result[key] = freq[key]
    
    return result