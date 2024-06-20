def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    stones = [n]
    curr_num = n
    
    while len(stones) < n:
        if curr_num % 2 == 0:
            stones.append(curr_num + 2)
        else:
            stones.append(curr_num + 1)
        curr_num = stones[-1]
    
    return stones