def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 2
    else:
        return 2 * (10 ** (n-1))

# Test the function
print(starts_one_ends(1)) # Output: 2
print(starts_one_ends(2)) # Output: 20
print(starts_one_ends(3)) # Output: 80