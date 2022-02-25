a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print(3)
elif d < 0:
    print(0)
elif d == 0:
    x = (-b + d**0.5) / (2 * a)
    print(1, x)
elif d > 0:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    print(2, min(x1, x2), max(x1, x2))
