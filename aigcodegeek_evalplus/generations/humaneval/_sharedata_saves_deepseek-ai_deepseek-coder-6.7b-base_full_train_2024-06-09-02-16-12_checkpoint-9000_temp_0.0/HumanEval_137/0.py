def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    # Check if a and b are strings and replace ',' with '.'
    if isinstance(a, str) and ',' in a:
        a = a.replace(',', '.')
    if isinstance(b, str) and ',' in b:
        b = b.replace(',', '.')

    # Convert a and b to float
    a = float(a)
    b = float(b)

    # Compare a and b and return the larger value or None
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None