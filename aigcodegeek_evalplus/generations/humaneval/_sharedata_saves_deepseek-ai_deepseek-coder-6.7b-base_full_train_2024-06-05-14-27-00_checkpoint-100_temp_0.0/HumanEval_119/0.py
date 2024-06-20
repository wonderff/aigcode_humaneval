def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # Step 1:  We need to check if it is possible to concatenate the two strings in some order to form a good string.
    # Step 2:  A good string is one where all parentheses are balanced.
    # Step 3:  We can start by counting the number of open and close parentheses in each string.
    # Step 4:  If the absolute difference between the counts is less than or equal to 1, then it is possible to form a good string.
    # Step 5:  Let's create a plan to implement the solution based on these thoughts.

    # Step 6:  Define a function to count the number of open and close parentheses in a string.
    def count_parens(s):
        open_count = 0
        close_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
        return open_count, close_count

    # Step 7:  Count the number of open and close parentheses in each string.
    open1, close1 = count_parens(lst[0])
    open2, close2 = count_parens(lst[1])

    # Step 8:  Check if the absolute difference between the counts is less than or equal to 1.
    if abs(open1 - close1) <= 1 and abs(open2 - close2) <= 1:
        return 'Yes'
    else:
        return 'No'