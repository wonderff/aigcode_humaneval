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
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            if char.islower():
                encoded_message += chr(ord(char) + 2)
            else:
                encoded_message += chr(ord(char.lower()) + 2).upper()
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    return encoded_message