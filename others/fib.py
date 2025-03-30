def fib(n):
    prev, curr = 1, 0
    k = 0
    while k < n:
        curr, prev = curr + prev, curr
        k = k + 1
    return curr
