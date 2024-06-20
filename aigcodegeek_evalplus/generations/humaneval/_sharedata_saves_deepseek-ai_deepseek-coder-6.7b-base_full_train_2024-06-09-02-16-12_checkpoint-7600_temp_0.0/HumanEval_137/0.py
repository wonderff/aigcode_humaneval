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
    # Check if a and b are of the same type
    if type(a) != type(b):
        return None

    # Convert strings to float if necessary
    if isinstance(a, str):
        a = a.replace(',', '.')
        a = float(a)

    if isinstance(b, str):
        b = b.replace(',', '.')
        b = float(b)

    # Compare the values
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None