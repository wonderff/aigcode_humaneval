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
    # Convert strings to float if possible
    if isinstance(a, str):
        try:
            a = float(a.replace(',', '.'))
        except ValueError:
            pass
    if isinstance(b, str):
        try:
            b = float(b.replace(',', '.'))
        except ValueError:
            pass

    # Compare values
    if a == b:
        return None
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        return a if a > b else b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        return a if float(b.replace(',', '.')) < b else b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return b if float(a.replace(',', '.')) < a else a