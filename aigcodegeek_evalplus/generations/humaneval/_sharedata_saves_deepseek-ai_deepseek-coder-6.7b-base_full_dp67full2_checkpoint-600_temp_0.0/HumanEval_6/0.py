from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    max_depth = []
    for group in groups:
        stack = []
        max_depth_group = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth_group = max(max_depth_group, len(stack))
            elif char == ')':
                stack.pop()
        max_depth.append(max_depth_group)
    return max_depth