def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7]
    count = 0
    for i in primes:
        if a % i == 0:
            count += 1
    return count == 3 and a > 1

is_multiply_prime(30)