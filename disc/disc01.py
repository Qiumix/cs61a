def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    #if raining or temp < 60:
    #    return True
    #else:
    #    return False
    return raining or temp < 60

'''
def square(x):
    print("here!")
    return x * x
def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
square(so_slow(5))
'This code's running time is longer than the universe.'
'''

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i <= n//2:
        if n % i == 0:
            return False
        i = i + 1
    return True