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
    
    # check if the file_name is empty
    if not file_name:
        return 'No'
    
    # check if the file_name contains more than three digits
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
        return 'No'
    
    # check if the file_name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    
    # split the file_name into two parts: before and after the dot
    file_name_split = file_name.split('.')
    
    # check if the first part before the dot starts with a letter from the latin alphabet
    if not file_name_split[0][0].isalpha():
        return 'No'
    
    # check if the second part after the dot is one of the allowed extensions
    if file_name_split[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'