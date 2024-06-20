def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Determine the lower and upper bounds of the range
    lower = min(a, b)
    upper = max(a, b)

    # Generate the even digits between the lower and upper bounds
    even_digits = [x for x in range(lower, upper + 1) if x % 2 == 0]

    return even_digits