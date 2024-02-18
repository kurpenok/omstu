count = 0

previous = 0

while True:
    n = int(input())
    if n:
        if previous and previous < n:
            count += 1
        previous = n
    else:
        print(count)
        break
