from math import sqrt

n = int(input())

amount = 0

for i in range(1, n):
    if not (n % i):
        amount += i

print(f'[+] Amount: {amount + n}')

