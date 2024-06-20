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
    sentences = S.replace("!", ".").replace("?", ".").split(".")
    
    # Initialize the count of boredoms
    boredom_count = 0
    
    # Iterate through each sentence
    for sentence in sentences:
        # Remove leading and trailing whitespace
        sentence = sentence.strip()
        
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the count of boredoms
            boredom_count += 1
    
    # Return the count of boredoms
    return boredom_count