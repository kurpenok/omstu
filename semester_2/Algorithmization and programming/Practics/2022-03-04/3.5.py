n = int(input())

powers_odd = []
powers_even = []

amount = 0

for i in range(1, n + 1):
    if i % 2:
        powers_odd.append(i)
        amount += pow(i, sum(powers_odd))
    else:
        powers_even.append(i)
        amount += pow(i, sum(powers_even))

print(amount)

