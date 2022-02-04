from math import sin, cos, pi, tan, sqrt

x = float(input("[>] Enter X: "))

l = 6.2

if x < 0:
    y = sin(x * pi)
    print("[+] Number of branch: 1")
elif 0 <= x <= 1:
    y = sqrt(abs(cos(x * pi)))
    print("[+] Number of branch: 2")
else:
    y = pow(tan(l * x), 2)
    print("[+] Number of branch: 3")

print(f"[+] Y: {y}")

