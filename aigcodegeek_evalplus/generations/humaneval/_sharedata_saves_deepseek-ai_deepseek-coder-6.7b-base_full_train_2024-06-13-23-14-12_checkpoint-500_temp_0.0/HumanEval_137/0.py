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
    # Check if both values are of the same type
    if type(a) == type(b):
        # Check if the values are equal
        if a == b:
            return None
        # Check if the values are strings
        elif isinstance(a, str) and isinstance(b, str):
            # Replace , with . in strings
            a = a.replace(',', '.')
            b = b.replace(',', '.')
            # Compare the floats
            if float(a) > float(b):
                return a
            else:
                return b
        # Compare the values if they are not strings
        else:
            return max(a, b)
    # If the values are of different types, return the larger type
    else:
        return max(type(a), type(b))