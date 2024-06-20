def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_digits = len(str(x))
    if shift > num_digits:
        return str(x)[::-1]
    else:
        return str(x)[shift:] + str(x)[:shift]