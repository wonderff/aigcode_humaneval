def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if the number is even
    if n % 2 != 0:
        return False

    # Check if the number is 4 or 8
    if n == 4 or n == 8:
        return True

    # Check if the number is greater than 8
    if n > 8:
        return False

    # Check if the number is 6, 7, or 9
    if n == 6 or n == 7 or n == 9:
        return True

    # If none of the above conditions are met, the number cannot be written as the sum of 4 positive even numbers
    return False