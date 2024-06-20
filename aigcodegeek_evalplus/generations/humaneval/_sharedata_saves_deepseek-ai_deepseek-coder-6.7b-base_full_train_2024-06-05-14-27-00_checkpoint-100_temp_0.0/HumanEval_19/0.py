from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map the numberals to their corresponding integers
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string into a list of numberals
    numberals = numbers.split()

    # Convert the numberals to integers and sort them
    sorted_numbers = sorted([number_map[num] for num in numberals])

    # Convert the sorted integers back to numberals
    sorted_numberals = [list(number_map.keys())[list(number_map.values()).index(num)] for num in sorted_numbers]

    # Join the sorted numberals into a space-delimited string
    sorted_string = ' '.join(sorted_numberals)

    return sorted_string