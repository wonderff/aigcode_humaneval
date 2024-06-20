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
    # Split the string into sentences
    sentences = [s.strip() for s in S.split('.') if s.strip()]
    # Initialize the boredom count
    boredom_count = 0
    # Iterate over the sentences
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the boredom count
            boredom_count += 1
    # Return the boredom count
    return boredom_count