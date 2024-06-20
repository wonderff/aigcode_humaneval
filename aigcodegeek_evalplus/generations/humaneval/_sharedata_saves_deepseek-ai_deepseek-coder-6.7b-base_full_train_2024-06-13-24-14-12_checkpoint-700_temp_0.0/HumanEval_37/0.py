def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [x for x in range(len(l)) if x % 2 == 0]
    sorted_even_values = sorted([l[i] for i in even_indices])
    result = l.copy()
    for i, val in zip(even_indices, sorted_even_values):
        result[i] = val
    return result