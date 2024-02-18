def get_divisors_count(number: int):
    c = 2
    for i in range(2, c):
        if not (number % i):
            c += 1
    return c


def get_max_divisions_number(n: int, m: int) -> int:
    maximum = n
    for i in range(n, m + 1):
        temp = get_divisors_count(i)
        if maximum < temp:
            temp = maximum
    return maximum

