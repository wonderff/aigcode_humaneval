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
    # Check if the values are equal
    if a == b:
        return None

    # Convert strings with floating point to float
    if isinstance(a, str) and '.' in a:
        a = float(a.replace(',', '.'))
    if isinstance(b, str) and '.' in b:
        b = float(b.replace(',', '.'))

    # Compare the values and return the larger one
    if a > b:
        return a
    else:
        return b