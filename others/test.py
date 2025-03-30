from math import pow
def small(n):
    t = 2
    while(t <= n):
        if (n % t == 0):
            return t
        t += 1
def print_factor(n):
    '''
    >>> print_factor(858)
    2
    3
    11
    12
    >>> print_factor(8)
    2
    2
    2
    >>> print_factor(9)
    3
    3
    >>> print_factor(10)
    2
    5
    '''
    t = small(n)
    print(t)
    n /= t
    if n == 1:
        return
    print_factor(n)
def f(x):
    assert x > 0 , "error:x is less than zero!"
    return pow(x, 0.5)

