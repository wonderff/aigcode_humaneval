import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the length of xs is even
    if len(xs) % 2 != 0:
        raise ValueError("The length of xs must be even")

    # Find the largest non-zero coefficient
    largest_coeff = max(xs)

    # Use the largest coefficient as the initial guess for the zero
    x = largest_coeff

    # Iterate using the Newton-Raphson method to find the zero
    while abs(poly(xs, x)) > 1e-6:
        # Calculate the derivative of the polynomial
        derivative = [i * coeff for i, coeff in enumerate(xs)]

        # Calculate the next guess using the Newton-Raphson formula
        x = x - poly(xs, x) / poly(derivative, x)

    return x