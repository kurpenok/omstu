n = int(input("[>] Enter number: "))

start = 0
while start < 3:
    n += n + 1
    n *= n + 1
    n += n + 1

    start += 1

print(f"[+] New number: {n}")

