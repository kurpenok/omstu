n = int(input())

amount = 0

for i in range(1, n + 1):
    if not (n % i):
        amount += i

print(amount)

