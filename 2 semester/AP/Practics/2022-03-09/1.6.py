a = set(map(int, input("[>] Enter first array: ").split()))
b = set(map(int, input("[>] Enter second array: ").split()))

intersection = a & b
union = a | b

print(f"[+] Result: {union - intersection}")

