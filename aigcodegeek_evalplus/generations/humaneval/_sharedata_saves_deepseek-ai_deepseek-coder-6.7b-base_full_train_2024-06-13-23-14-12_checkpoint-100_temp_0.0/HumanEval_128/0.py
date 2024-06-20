def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if len(arr) == 0:
        return None
    else:
        product = 1
        sum_magnitude = 0
        for num in arr:
            if num > 0:
                product *= 1
            elif num < 0:
                product *= -1
            else:
                product *= 0
            sum_magnitude += abs(num)
        return product * sum_magnitude