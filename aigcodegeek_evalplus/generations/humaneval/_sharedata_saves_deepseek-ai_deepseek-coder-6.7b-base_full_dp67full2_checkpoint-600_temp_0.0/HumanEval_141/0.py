def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check if the file name contains more than three digits
    if len(file_name) > 3:
        return 'No'
    
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into the substring before and after the dot
    name_parts = file_name.split('.')
    name_before_dot = name_parts[0]
    name_after_dot = name_parts[1]
    
    # Check if the substring before the dot is empty or starts with a digit
    if len(name_before_dot) == 0 or name_before_dot[0].isdigit():
        return 'No'
    
    # Check if the substring after the dot is one of the allowed types
    allowed_types = ['txt', 'exe', 'dll']
    if name_after_dot not in allowed_types:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'