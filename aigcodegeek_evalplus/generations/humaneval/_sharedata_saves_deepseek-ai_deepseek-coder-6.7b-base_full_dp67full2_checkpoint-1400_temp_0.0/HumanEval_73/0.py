def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Initialize two pointers, one at the beginning of the array and one at the end
    left, right = 0, len(arr) - 1
    changes = 0

    # Iterate through the array until the two pointers meet
    while left < right:
        # If the elements at the two pointers are not equal, we need to change one of them
        if arr[left] != arr[right]:
            changes += 1
        # Move the pointers towards each other
        left += 1
        right -= 1

    return changes