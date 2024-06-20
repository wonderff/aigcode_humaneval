def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) < 2:
        return None
    min_num = float('inf')
    second_min = float('inf')
    for num in lst:
        if num < min_num:
            second_min = min_num
            min_num = num
        elif num < second_min and num != min_num:
            second_min = num
    return second_min if second_min < float('inf') else None