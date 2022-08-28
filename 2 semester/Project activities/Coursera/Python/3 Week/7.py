p = int(input())
x = int(input())
y = int(input())
k = int(input())

i = 0

while i != k:
    i += 1
    x *= p * 0.01 + 1
    y *= p * 0.01 + 1
    k2 = y * 0.01 + x + 10**-7
    x = int(k2)
    y = int(100 * (k2 - x))

print(x, y)
