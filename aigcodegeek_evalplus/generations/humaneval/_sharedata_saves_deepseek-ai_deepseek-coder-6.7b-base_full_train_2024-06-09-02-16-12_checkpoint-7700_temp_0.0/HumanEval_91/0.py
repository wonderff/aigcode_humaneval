def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences based on '.', '?' or '!'
    sentences = []
    start = 0
    for i, char in enumerate(S):
        if char in ['.', '?', '!']:
            sentences.append(S[start:i+1].strip())
            start = i+1
    sentences.append(S[start:].strip())

    # Count the number of boredoms
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith("I"):
            boredom_count += 1

    return boredom_count