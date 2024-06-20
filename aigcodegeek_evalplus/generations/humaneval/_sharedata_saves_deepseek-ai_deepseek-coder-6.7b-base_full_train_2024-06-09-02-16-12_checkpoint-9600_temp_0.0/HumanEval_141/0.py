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
    import re

    # Check if there are more than three digits in the file name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into the name part and extension part
    name_part, extension = file_name.split('.')

    # Check if the name part is empty or does not start with a latin alphapet letter
    if not name_part or not name_part[0].isalpha():
        return 'No'

    # Check if the extension is one of the allowed extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'