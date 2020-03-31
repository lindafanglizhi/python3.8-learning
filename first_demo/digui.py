def sum_number(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


sum_number(100)


def sum_number1(n):
    if n <= 0:
        return 0
    return n+sum_number1(n-1)


print(sum_number1(100))