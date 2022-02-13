rabbits = int(input("[>] Enter count of rabbits: "))

number_1 = number_2 = 1
index = 0

while True:
    if number_2 == rabbits:
        print(f"[+] Index in sequence: {index}")
        break
    elif number_2 > rabbits:
        print("[-] No")
        break
    number_1, number_2 = number_2, number_1 + number_2
    count += 1

