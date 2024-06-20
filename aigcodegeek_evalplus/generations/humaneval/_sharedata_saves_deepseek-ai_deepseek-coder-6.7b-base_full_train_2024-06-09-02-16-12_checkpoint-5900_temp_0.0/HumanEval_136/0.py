def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    neg_integers = [num for num in lst if num < 0]
    pos_integers = [num for num in lst if num > 0]

    if not neg_integers:
        neg_max = None
    else:
        neg_max = max(neg_integers)

    if not pos_integers:
        pos_min = None
    else:
        pos_min = min(pos_integers)

    return (neg_max, pos_min)