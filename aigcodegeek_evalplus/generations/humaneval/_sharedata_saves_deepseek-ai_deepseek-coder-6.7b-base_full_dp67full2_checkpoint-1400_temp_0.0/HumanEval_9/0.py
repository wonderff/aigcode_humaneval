from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    max_list = []
    
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        max_list.append(max_so_far)
    
    return max_list