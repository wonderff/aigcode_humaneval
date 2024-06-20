from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def find_depth(s):
        count = 0
        max_count = 0
        for ch in s:
            if ch == '(':
                count += 1
                max_count = max(max_count, count)
            elif ch == ')':
                count -= 1
        return max_count

    groups = paren_string.split()
    depths = [find_depth(group) for group in groups]
    return depths