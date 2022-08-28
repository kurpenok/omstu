from math import sqrt

n = int(input("[>] Enter square: "))

for i in range(1, int(sqrt(n)) + 1):
    if not (n % i):
        print(f"{i} {n // i}")

