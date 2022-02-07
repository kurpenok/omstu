n = int(input())

if n >= 10 and n <= 20:
    print(f"{n} korov")
elif n % 10 == 1:
    print(f"{n} korova")
elif n % 10 >= 2 and n % 10 <= 4:
    print(f"{n} korovy")
elif n % 10 == 0 or (n % 10 >= 5 and n % 10 <= 9):
    print(f"{n} korov")
