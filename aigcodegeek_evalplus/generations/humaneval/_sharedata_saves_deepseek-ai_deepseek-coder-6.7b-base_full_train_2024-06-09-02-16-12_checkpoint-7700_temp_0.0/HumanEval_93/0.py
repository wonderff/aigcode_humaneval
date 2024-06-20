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
            if char.lower() == 'a':
                encoded_message += 'C'
            elif char.lower() == 'e':
                encoded_message += 'G'
            elif char.lower() == 'i':
                encoded_message += 'K'
            elif char.lower() == 'o':
                encoded_message += 'Q'
            elif char.lower() == 'u':
                encoded_message += 'W'
        else:
            encoded_message += char.swapcase()
    return encoded_message