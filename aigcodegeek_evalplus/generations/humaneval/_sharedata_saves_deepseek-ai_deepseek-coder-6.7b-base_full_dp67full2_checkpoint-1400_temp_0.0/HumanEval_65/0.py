def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    n = len(digits)
    if shift >= n:
        return digits[::-1]
    else:
        return digits[n-shift:] + digits[:n-shift]

print(circular_shift(12, 1)) # "21"
print(circular_shift(12, 2)) # "12"
print(circular_shift(12345, 3)) # "23451"
print(circular_shift(12345, 4)) # "12345"