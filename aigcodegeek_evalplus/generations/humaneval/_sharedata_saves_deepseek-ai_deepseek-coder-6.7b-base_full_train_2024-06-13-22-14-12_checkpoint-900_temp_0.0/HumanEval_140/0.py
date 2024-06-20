def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = ''
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                result += '-'
            else:
                result += '_'
        else:
            count = 0
            result += char
    return result