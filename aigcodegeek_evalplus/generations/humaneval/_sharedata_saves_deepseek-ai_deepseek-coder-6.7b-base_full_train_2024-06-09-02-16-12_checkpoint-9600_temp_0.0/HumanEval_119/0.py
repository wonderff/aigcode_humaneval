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
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack

    s1, s2 = lst
    for i in range(len(s1)):
        for j in range(len(s2)):
            if is_balanced(s1[i:] + s2[j:]):
                return 'Yes'
    return 'No'