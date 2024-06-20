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
    def is_balanced(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def helper(s1, s2):
        if is_balanced(s1) and is_balanced(s2):
            return 'Yes'
        elif len(s1) == 0 and len(s2) == 0:
            return 'No'
        elif len(s1) > 0 and is_balanced(s1):
            return helper('', s2)
        elif len(s2) > 0 and is_balanced(s2):
            return helper(s1, '')
        else:
            return helper(s1[1:], s2) or helper(s1, s2[1:])

    return helper(lst[0], lst[1])