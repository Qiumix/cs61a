from math import sqrt, pi
def area(r, shape):
    assert r > 0, 'r cann\'t be negative!'
    return r * r * shape
def hex(r):
    return area(r, 3 * sqrt(3) / 2)
def circle(r):
    return area(r, pi)
def squ(r):
    return area(r, 1)
def sum_naturals(n):
    """Sum the first N natural numbers.
    
    >>> sum_naturals(5)
    15
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + i, i + 1
    return total
def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    
    >>> sum_cubes(5)
    225
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + pow(i, 3), i + 1
    return total
def identity(n):
    return n
def cube(n):
    return n * n * n
def summation(n, term):
    """
    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + term(i), i + 1
    return total
def pi_term(n):
    return 8 / ((4 * n - 1) * (4 * n - 3))
def make_adder(n):
    def adder(k):
        return k * k + n
    return adder
def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1
square = lambda x: x * x
def inverse(f):
    return lambda y: search(lambda x:f(x) == y)
sqrt = inverse(square)