def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n - 1)


def hailstone(n):
    """Printoutthehailstonesequencestartingatn,andreturnthe
    numberof elementsinthesequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print(1)
        return 1
    if n % 2:
        print(n)
        return 1 + hailstone(n * 3 + 1)
    else:
        print(n)
        return 1 + hailstone(n // 2)


def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    max, min = n1 % 10, n2 % 10
    if max < min:
        max, min = min, max
        return min + 10 * merge(n1 // 10, n2)
    return min + 10 * merge(n1, n2 // 10)

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(y):
        if y:
            return f(repeat(y - 1))
        else:
            return x
    return repeat