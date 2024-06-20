def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [int(d) for d in str(x)]
    if shift > len(digits):
        return ''.join(str(d) for d in reversed(digits))
    else:
        return ''.join(str(d) for d in digits[-shift:] + digits[:-shift])