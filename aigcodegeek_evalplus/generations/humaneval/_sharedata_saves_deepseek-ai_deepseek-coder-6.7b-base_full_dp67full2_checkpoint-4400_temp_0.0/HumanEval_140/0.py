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
    
    # Replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # Replace consecutive underscores with a single underscore
    while '__' in text:
        text = text.replace('__', '_')
    
    # Replace consecutive dashes with a single dash
    while '-' in text:
        text = text.replace('-', '_')
    
    return text