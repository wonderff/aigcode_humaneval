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

    # Check if a and b are integers or floats
    if isinstance(a, (int, float)):
        # Compare a and b and return the larger one
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

    # Check if a and b are strings
    if isinstance(a, str):
        # Remove the comma from a and b
        a = a.replace(",", "")
        b = b.replace(",", "")

        # Convert a and b to floats
        a = float(a)
        b = float(b)

        # Compare a and b and return the larger one
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None