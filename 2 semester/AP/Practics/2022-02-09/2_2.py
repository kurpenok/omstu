n = int(input("[>] Enter N: "))
m = int(input("[>] Enter M: "))

if n % m:
    print(f"[+] Kilometers: {n // m + 1}")
else:
    print(f"[+] Kilometers: {n // m}")

