def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ""
    for char in s:
        if char.isalpha():
            shift = 2
            char_code = ord(char.lower()) - 97 + shift
            if char.isupper():
                if char_code > 25:
                    char_code -= 26
            else:
                if char_code > 25:
                    char_code -= 26
            result += chr(char_code + 97)
        else:
            result += char
    return result