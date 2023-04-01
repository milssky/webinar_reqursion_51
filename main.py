def F(n):
    if n <= 5:
        return n
    if n % 5 == 0:
        return n + F(n//5 + 1)
    return n + F(n+6)
    # return n + F(n // 5 + 1) if n % 5 == 0 else n + F(n + 6)


for number in range(1000):
    try:
        result = F(number)
    except RecursionError:
        continue
    else:
        if result > 1000:
            print(number)
            break
