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
    result = []
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                result.append('-')
        else:
            if count > 0:
                if count == 2:
                    result.append('_')
                result.append(char)
                count = 0
            else:
                result.append(char)
    return ''.join(result)

# Test cases
print(fix_spaces("Example")) # "Example"
print(fix_spaces("Example 1")) # "Example_1"
print(fix_spaces(" Example 2")) # "_Example_2"
print(fix_spaces(" Example   3")) # "_Example-3"