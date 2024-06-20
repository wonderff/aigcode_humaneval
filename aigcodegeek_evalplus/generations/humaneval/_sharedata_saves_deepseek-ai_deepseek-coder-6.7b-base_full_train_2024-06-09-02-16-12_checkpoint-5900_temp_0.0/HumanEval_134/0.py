def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and (txt[-2] == ' ' or txt[-2] == '\n' or txt[-2] == '\t' or txt[-2] == '\r' or txt[-2] == '\f' or txt[-2] == '\v' or txt[-2] == '\b' or txt[-2] == '\0'):
        return True
    else:
        return False