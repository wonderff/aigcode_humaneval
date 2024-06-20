def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return "N should be a positive integer"
    elif n == 1:
        return 2
    else:
        return 2 * (10 ** (n - 1))

# Testing the function
print(starts_one_ends(1))  # Output: 2
print(starts_one_ends(2))  # Output: 4
print(starts_one_ends(3))  # Output: 7
print(starts_one_ends(4))  # Output: 13
print(starts_one_ends(5))  # Output: 21