max_1 = 0
max_2 = 0

while True:
    number = int(input("[>] Enter number: "))
    if number > 1000:
        break
    if number > max_1:
        max_2 = max_1
        max_1 = number

print(f"[+] Second maximum in sequence: {max_2}")

