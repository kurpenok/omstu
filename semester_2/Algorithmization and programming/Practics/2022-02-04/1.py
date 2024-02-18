from math import sqrt, sin, cos, tan, log10, e, pi

x = 5

z1 = (1 + 2.5 * x) / (x**2 * (1 - x))

z2 = sqrt(x) * sqrt(abs(1 - x)) * pow(x**2 + 1, 1/3) * pow(abs(sin(x)), 1/4)

z3 = pow(sin(sqrt(x)), 3)

z4 = log10(1 + x) + log10(5) + cos(pi / 12)

z5 = pow(e, 2) + pow(e, tan(x))

print(f"[+] Z1: {z1:5.3f}")
print(f"[+] Z2: {z2:5.3f}")
print(f"[+] Z3: {z3:5.3f}")
print(f"[+] Z4: {z4:5.3f}")
print(f"[+] Z5: {z5:5.3f}")

