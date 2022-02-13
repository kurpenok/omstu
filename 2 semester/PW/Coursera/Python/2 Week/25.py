n = int(input())

index = 1

while True:
    if index**2 > n:
        break
    print(index**2, end=" ")
    index += 1
