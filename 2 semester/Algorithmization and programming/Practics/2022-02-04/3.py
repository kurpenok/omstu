from math import sqrt, log10, cos, log, e

# x = float(input("[>] Enter X variable: "))
# y = float(input("[>] Enter Y variable: "))
# d = float(input("[>] Enter D variable: "))

x = 3.5
y = 3.8
d = 4.9

s = sqrt(log10(x) + pow(cos(x), 2))
w = (pow(log(pow(x, 3)) + x * y, 1 / 3)) / (abs(d - 2 * x)) + pow(e, 3 - x)
r = abs(s**2 - w**2)

print(f"[+] S: {s:1.2f}")
print(f"[+] W: {w:1.2f}")
print(f"[+] R: {r:1.2f}")
 
