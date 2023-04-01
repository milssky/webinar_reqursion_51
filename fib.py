# 1 1 2 3 5 8 13 21 34 ...
cache = {}


def fib(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result


print(fib(99))
