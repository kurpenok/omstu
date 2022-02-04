from math import sqrt, tan, log

x = float(input("[>] Enter X: "))

a = 5 * 10**(-3)

if x > 4.5:
    z = sqrt(abs(a + x) + 1 / tan(x))
else:
    z = pow(x, 1 / 3) + pow(log(x + 2), 2)

print(f"[+] X: {x:5.1f}")
print(f"[+] Z: {z:5.3f}")

