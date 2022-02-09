hour = int(input())

if hour == 23 or hour <= 4:
    print("Night")
elif  5 <= hour <= 10:
    print("Morning")
elif 11 <= hour <= 17:
    print("Day")
elif 18 <= hour <= 22:
    print("Tonight")

