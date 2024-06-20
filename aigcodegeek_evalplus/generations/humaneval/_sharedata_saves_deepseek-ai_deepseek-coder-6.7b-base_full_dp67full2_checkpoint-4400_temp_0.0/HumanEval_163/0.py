def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the minimum and maximum values of a and b
    min_val = min(a, b)
    max_val = max(a, b)

    # Filter out the even numbers between min_val and max_val
    even_numbers = filter(lambda x: x % 2 == 0, range(min_val, max_val + 1))

    # Return the sorted list of even numbers
    return sorted(even_numbers)