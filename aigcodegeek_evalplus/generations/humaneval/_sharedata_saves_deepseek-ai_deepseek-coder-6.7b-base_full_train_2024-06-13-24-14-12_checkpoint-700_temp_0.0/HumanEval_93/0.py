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
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        elif char.lower() in vowels:
            vowel_index = vowels.index(char.lower())
            encoded_message += vowels[(vowel_index + 2) % 5]
        else:
            encoded_message += char
    return encoded_message