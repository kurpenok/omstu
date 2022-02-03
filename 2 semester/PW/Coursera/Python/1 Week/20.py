n = int(input())
m = int(input())

if (m / n).is_integer():
    print(m // n)
else:
    print(m // n + 1)
