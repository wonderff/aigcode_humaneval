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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            index = (alphabet.index(char.lower()) + 2) % 26
            if char.isupper():
                encoded_message += alphabet[index].upper()
            else:
                encoded_message += alphabet[index]
        else:
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
    return encoded_message