def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    if n === 1:
        return 2 # 1 and 0 are the only two numbers that start or end with 1
    return 2 * 2**(n-1)