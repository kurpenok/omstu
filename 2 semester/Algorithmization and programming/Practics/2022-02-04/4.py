k, p = map(int, input("[>] Enter K and P: ").split())

if p % 2 and k % 3 == p:
    print(f"[+] Result: {p**2 + k**2}")
else:
    k = 0
    p = 0

