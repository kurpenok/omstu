money_type = input()
money = int(input())

if money_type == "фунт стерлингов":
    print(f"Фунтов: {money}")
    print(f"Шиллинг: {money * 20}")
    print(f"Пенсов: {money * 240}")
    print(f"Фартинг: {money * 960}")
elif money_type == "шиллинг":
    print(f"Фунтов: {money // 20}")
    print(f"Шиллинг: {money}")
    print(f"Пенсов: {money * 12}")
    print(f"Фартинг: {money * 4}")
elif money_type == "пенсы":
    print(f"Фунтов: {money // 240}")
    print(f"Шиллинг: {money // 12}")
    print(f"Пенсов: {money}")
    print(f"Фартинг: {money * 4}")
elif money_type == "фартинг":
    print(f"Фунтов: {money // 960}")
    print(f"Шиллинг: {money // 240}")
    print(f"Пенсов: {money // 20}")
    print(f"Фартинг: {money}")

