n = float(input())

whole = int(n)
fractional = int(round((n % 1), 2) * 100)

print(whole, fractional)
