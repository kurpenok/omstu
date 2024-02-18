n = int(input())

amount = 0

for i in range(1, n + 1):
    amount += (1 / i**2)

print(amount)
