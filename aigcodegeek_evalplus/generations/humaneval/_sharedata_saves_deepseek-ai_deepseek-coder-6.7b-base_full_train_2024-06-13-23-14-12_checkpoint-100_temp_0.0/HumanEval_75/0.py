def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(4))  # False
print(is_multiply_prime(15))  # False
print(is_multiply_prime(21))  # False
print(is_multiply_prime(25))  # False
print(is_multiply_prime(27))  # True
print(is_multiply_prime(35))  # False
print(is_multiply_prime(45))  # False
print(is_multiply_prime(51))  # False
print(is_multiply_prime(53))  # True