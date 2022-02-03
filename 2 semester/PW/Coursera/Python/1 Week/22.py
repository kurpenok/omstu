n = input()

n = "0" * (4 - len(n)) + n

if n == n[::-1]:
    print(1)
else:
    print(0)
