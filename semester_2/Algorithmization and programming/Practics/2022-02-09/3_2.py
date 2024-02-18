count = 0

while True:
    number = float(input("[>] Enter real number: "))
    if number <= 36.6:
        if number < 0:
            count += 1
    else:
        break

print(f"[>] Count of negative numbers: {count}")

