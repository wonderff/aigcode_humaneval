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
    def count_changes(i, j):
        if i >= j:
            return 0
        if arr[i] == arr[j]:
            return count_changes(i+1, j-1)
        else:
            return 1 + count_changes(i+1, j-1)

    return count_changes(0, len(arr)-1)