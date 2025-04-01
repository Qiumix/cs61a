def rational(n, m):
    from fractions import gcd
    g = gcd(n, m)
    return [n // g, m // g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def add_rationals(s1, s2):
    """
    >>> half = rational(1, 2)
    >>> print_rational(half)
    1 / 2
    >>> third = rational(1, 3)
    >>> print_rational(mul_rationals(half, third))
    1 / 6
    >>> print_rational(add_rationals(third, third))
    2 / 3
    """
    return rational(numer(s1) * denom(s2) + numer(s2) * denom(s1), denom(s1) * denom(s2))


def mul_rationals(s1, s2):
    return rational(numer(s1) * numer(s2), denom(s1) * denom(s2))


def rationals_is_equal(s1, s2):
    return numer(s1) * denom(s2) == numer(s2) * denom(s1)


def print_rational(s):
    """
    >>> half = rational(1, 2)
    >>> print_rational(half)
    1 / 2
    >>> third = rational(1, 3)
    >>> print_rational(mul_rationals(half, third))
    1 / 6
    >>> print_rational(add_rationals(third, third))
    2 / 3
    """
    print(numer(s), "/", denom(s))


def square_rational(s):
    return rational(numer(s) ** 2, denom(s) ** 2)

    
