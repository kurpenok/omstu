h = int(input())
a = int(input())
b = int(input())

days = 0

while True:
    days += 1
    h -= a
    if h <= 0:
        print(days)
        break
    h += b
