start = int(input())
step = int(input())
stop = int(input())

for i in range(start, stop - step, -step):
    print(f"[+] Height: {i}")

print("[+] Glissade")

