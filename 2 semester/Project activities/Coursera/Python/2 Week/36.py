count = 0

while True:
    n = int(input())
    if n:
        if not (n % 2):
            count += 1
    else:
        print(count)
        break
