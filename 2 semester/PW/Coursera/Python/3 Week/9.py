a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (b * f - d * e) / (b * c - a * d)

if b:
    y = (e - a * x) / b
else:
    y = (f - c * x) / d

print(x, y)
