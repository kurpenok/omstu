a = list(map(int, input("[>] Enter array: ").split()))

print(f"[+] Maximum: {max(a)}")
print(f"[+] Minimum: {min(a)}")
print(f"[+] Amount: {sum(a)}")
print(f"[+] Average: {sum(a) / len(a)}")

a.remove(min(a))
print(f"[+] Second minimum: {min(a)}")

