x = int(input())
y = int(input())

day = 1

while True:
    if x >= y:
        print(day)
        break
    x *= 1.1
    day += 1
