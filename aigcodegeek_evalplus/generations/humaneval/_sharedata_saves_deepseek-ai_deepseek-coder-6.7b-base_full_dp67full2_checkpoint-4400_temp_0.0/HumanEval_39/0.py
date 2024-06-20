def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n: int):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

    i = 2
    while True:
        if is_prime(fibonacci(i)):
            n -= 1
            if n == 0:
                return fibonacci(i)
        i += 1

print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))