def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * (10 ** (n - 1))