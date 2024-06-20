def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    encoded_message = ""
    for char in message:
        if char in vowels:
            encoded_message += chr(ord(char) + 2)
        elif char.isupper():
            encoded_message += char.lower()
        elif char.islower():
            encoded_message += char.upper()
    return encoded_message