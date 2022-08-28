n = int(input("[>] Enter number: "))

start = 0
temp = n

while start < 4:
    temp += 1
    n += temp
    
    temp += 1
    n *= temp

    start += 1

print(f"[+] New number: {n}")

