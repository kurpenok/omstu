amount = 0
count = 0

while True:
    n = int(input())
    if n:
        amount += n
        count += 1
    else:
        print(amount / count)
        break
