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
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def concatenate(s1, s2):
        return s1 + s2

    def concatenate_reversed(s1, s2):
        return s2 + s1

    def try_concatenate(s1, s2):
        if is_balanced(concatenate(s1, s2)):
            return 'Yes'
        if is_balanced(concatenate_reversed(s1, s2)):
            return 'Yes'
        return 'No'

    return try_concatenate(lst[0], lst[1])