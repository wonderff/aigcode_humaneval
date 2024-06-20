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
    hist = {}
    max_count = 0
    for letter in test:
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1
        max_count = max(max_count, hist[letter])

    result = {}
    for letter, count in hist.items():
        if count == max_count:
            result[letter] = count

    return result