city_1 = input("[>] Enter first city: ")
city_2 = input("[>] Enter second city: ")

if city_1 != city_2 or (city_1 == "Тула" and city_2 == "Пенза"):
    print("[+] YES")
else:
    print("[-] NO")

