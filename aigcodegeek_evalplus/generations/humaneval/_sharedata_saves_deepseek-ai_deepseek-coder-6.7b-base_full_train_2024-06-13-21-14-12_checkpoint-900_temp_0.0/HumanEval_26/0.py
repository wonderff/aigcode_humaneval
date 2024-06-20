from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = {}
    result = []
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            result.append(num)
    return result