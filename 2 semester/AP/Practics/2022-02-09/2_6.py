money_type = input("[>] Enter type of money: ")
money = int(input("[>] Enter count of money: "))

if money_type == "фунт стерлингов":
    print(f"[+] Pound sterling: {money}")
    print(f"[+] Shilling: {money * 20}")
    print(f"[+] Pence: {money * 240}")
    print(f"[+] Farthing: {money * 960}")
elif money_type == "шиллинг":
    print(f"[+] Pound sterling: {money // 20}")
    print(f"[+] Shilling: {money}")
    print(f"[+] Pence: {money * 12}")
    print(f"[+] Farthing: {money * 48}")
elif money_type == "пенсы":
    print(f"[+] Pound sterling: {money // 240}")
    print(f"[+] Shilling: {money // 12}")
    print(f"[+] Pence: {money}")
    print(f"[+] Farthing: {money * 4}")
elif money_type == "фартинг":
    print(f"[+] Pound sterling: {money // 960}")
    print(f"[+] Shilling: {money // 48}")
    print(f"[+] Pence: {money // 4}")
    print(f"[+] Farthing: {money}")

