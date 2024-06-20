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
    negative_nums = [num for num in lst if num < 0]
    positive_nums = [num for num in lst if num > 0]

    if not negative_nums:
        return None, None
    elif not positive_nums:
        return None, None
    else:
        return max(negative_nums), min(positive_nums)