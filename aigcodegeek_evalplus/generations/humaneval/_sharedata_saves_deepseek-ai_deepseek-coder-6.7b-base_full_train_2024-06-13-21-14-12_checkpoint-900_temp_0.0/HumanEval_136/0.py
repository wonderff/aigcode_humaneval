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
    neg_max = None
    pos_min = None
    for num in lst:
        if num < 0:
            if neg_max is None or num > neg_max:
                neg_max = num
        elif num > 0:
            if pos_min is None or num < pos_min:
                pos_min = num
    return (neg_max, pos_min)