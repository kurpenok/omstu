from math import sqrt


def IsPrime(n: int) -> bool:
    if n in [1, 2, 3, 5, 7, 11]:
        return True
    for i in range(2, int(sqrt(n)) + 2):
        if not (n % i):
            return False
    return True


n = int(input())

if IsPrime(n):
    print('YES')
else:
    print('NO')
