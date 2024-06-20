def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    factors = []
    for prime in prime_numbers:
        while a % prime == 0:
            factors.append(prime)
            a = a // prime
    return len(factors) == 3 and set(factors) == set(prime_numbers)

print(is_multiply_prime(30)) # True
print(is_multiply_prime(45)) # False