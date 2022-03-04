from math import sqrt


def MinDivisor(n: int) -> int:
    for i in range(2, int(sqrt(n)) + 2):
        if not (n % i):
            return i
    return n


n = int(input())

print(MinDivisor(n))
