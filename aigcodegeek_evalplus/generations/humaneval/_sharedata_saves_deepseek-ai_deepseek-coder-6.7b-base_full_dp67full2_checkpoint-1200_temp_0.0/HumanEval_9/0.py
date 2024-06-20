from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements = []
    max_element = numbers[0]
    for number in numbers:
        max_element = max(max_element, number)
        max_elements.append(max_element)
    return max_elements