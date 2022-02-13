max_1 = 0
max_2 = 0

while True:
    n = int(input())
    if n:
        if n > max_1:
            max_2 = max_1
            max_1 = n
        elif n > max_2:
            max_2 = n
    else:
        print(max_2)
        break
