n = int(input())

amount = (n // 100) + ((n - (n // 100) * 100) // 10) + (n % 10)

print(amount)
