def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    factors = []
    for i in range(2, a):
        while a % i == 0:
            factors.append(i)
            a //= i
        if len(factors) > 3:
            return False
    return len(factors) == 3 and all(factor in [2, 3, 5] for factor in factors)