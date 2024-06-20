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
            ascii_offset = 97 if char.islower() else 65
            encrypted_char = chr((ord(char) - ascii_offset - 2) * 2 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result