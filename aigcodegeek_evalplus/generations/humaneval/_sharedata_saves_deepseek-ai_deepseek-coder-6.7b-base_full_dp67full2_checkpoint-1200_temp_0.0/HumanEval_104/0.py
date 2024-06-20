def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Create an empty list to store the unique digits
    unique_digits_list = []

    # Iterate through each number in the input list
    for num in x:
        # Convert the number to a string
        num_str = str(num)

        # Check if any digit in the number is even
        is_even_digit = False
        for digit in num_str:
            # Convert the digit back to an integer
            digit_num = int(digit)

            # If the digit is even, set is_even_digit to True and break the loop
            if digit_num % 2 == 0:
                is_even_digit = True
                break

        # If no even digit is found, add the number to the unique_digits_list
        if not is_even_digit:
            unique_digits_list.append(num)

    # Sort the unique_digits_list in increasing order
    unique_digits_list.sort()

    # Return the sorted unique_digits_list
    return unique_digits_list