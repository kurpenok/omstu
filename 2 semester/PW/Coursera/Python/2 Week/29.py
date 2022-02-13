n = int(input())

number = 1
power = 0

while True:
    if number >= n:
        print(power)
        break
    number *= 2
    power += 1
