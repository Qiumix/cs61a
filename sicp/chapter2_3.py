def test1():
    test_digit = [1, 8, 7, 6]
    print("test:", [2, 7, test_digit] + test_digit * 2)


# def test2():
#     """
#     >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
#     >>> same_count = 0
#     >>> for x, y in pairs:
#             if x == y:
#                 same_count = same_count + 1
#     >>> same_count
#     2
#     """


def test_range_list():
    """
    >>> range(5, 8)
    range(5, 8)
    >>> list(range(2, 5))
    [2, 3, 4]
    >>> list(range(4))
    [0, 1, 2, 3]
    """


# def go_bears():
#     """
#     >>> for _ in range(3):
#             print("go bears!")
#     go bears!
#     go bears!
#     go bears!
#     """

def odd():
    """"
    >>> odds = [1, 3, 5, 7]
    >>> [x + 1 for x in odds]
    [2, 4, 6, 8]
    >>> [x + 1 for x in odds if 25 % x == 0]
    [2, 6]
    """
    # [<map expression> for <name> in <sequence expression> if <filter expression>]


def devisors(n):
    # """
    # >>> divisors(4)
    # [1, 2]
    # >>> divisors(12)
    # [1, 2, 3, 4, 6]
    # >>> [for i in range(1, 1000) if sum(devisors(n)) == n]
    # [1, 6, 28, 464]
    # """
    return [1] + [x for x in range(2, n) if n % x == 0]


def get_w(area, h):
    assert area % h == 0
    return area // h


def get_c(w, h):
    return w * 2 + h * 2


def min_c(area):
    """
    >>> min_c(80)
    36
    """
    hs = devisors(area)
    return min([get_c(get_w(area, h), h) for h in hs])