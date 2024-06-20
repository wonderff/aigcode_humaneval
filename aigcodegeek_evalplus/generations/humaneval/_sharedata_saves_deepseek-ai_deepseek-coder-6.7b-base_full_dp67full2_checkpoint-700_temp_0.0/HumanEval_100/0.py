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
    # Initialize an empty list to store the number of stones in each level
    levels = []

    # Iterate through the levels of stones
    for i in range(n):
        # Calculate the number of stones in the current level
        if i % 2 == 0:
            # If the level is even, the number of stones is the next even number
            stones = (i + 2) * (i + 1)
        else:
            # If the level is odd, the number of stones is the next odd number
            stones = (i + 1) * (i + 2)

        # Append the number of stones to the list
        levels.append(stones)

    # Return the list of levels
    return levels