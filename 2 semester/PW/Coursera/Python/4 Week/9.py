from math import gcd


def ReduceFraction(n: int, m: int) -> tuple:
    k = gcd(n, m)
    return n // k, m // k


n = int(input())
m = int(input())

result = ReduceFraction(n, m)

print(result[0], result[1])
