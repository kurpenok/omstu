from math import pi, sin

x = 12.3 * 10**(-1)

y = 15.4

z = 0.252 * 10**3

g = (pow(y, x + 1) / (pow(abs(y - 2), 1/3) + 3)) +\
        ((x + y / 2) / (2 * abs(x + y))) * (pow(x + 1, -1 / sin(z)))

print(x, y, z)
print(f"[+] G: {g:2.4f}")

