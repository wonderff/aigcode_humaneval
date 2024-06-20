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
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(num):
        if num < 0:
            return None
        elif num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num-1) + fib(num-2)

    count = 0
    num = 0
    while count < n:
        if is_prime(fib(num)):
            count += 1
        num += 1
    return fib(num-1)