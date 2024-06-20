def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # Convert each number to binary and count the number of ones
    binary_counts = [bin(num).count('1') for num in arr]

    # Create a list of tuples where each tuple contains the number and its binary count
    num_binary_counts = list(zip(arr, binary_counts))

    # Sort the list of tuples based on the binary count and then the decimal value
    sorted_nums = sorted(num_binary_counts, key=lambda x: (x[1], x[0]))

    # Extract the sorted numbers from the tuples
    sorted_arr = [num for num, _ in sorted_nums]

    return sorted_arr