name = input()
email = input()

if "@" not in name and "@" in email:
    print("OK")
elif "@" not in name and "@" not in email:
    print("Некорректный адрес")
elif "@" in name and "@" in email:
    print("Некорректный логин")
elif "@" in name and "@" not in email:
    print("Все данне введены неверно")

