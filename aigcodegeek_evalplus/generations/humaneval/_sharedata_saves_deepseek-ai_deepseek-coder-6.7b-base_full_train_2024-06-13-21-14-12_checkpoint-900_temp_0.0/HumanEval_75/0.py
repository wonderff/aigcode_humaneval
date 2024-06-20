def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)

    if len(prime_factors) < 3:
        return False

    for i in range(len(prime_factors) - 2):
        if prime_factors[i] * prime_factors[i+1] * prime_factors[i+2] == a:
            return True

    return False