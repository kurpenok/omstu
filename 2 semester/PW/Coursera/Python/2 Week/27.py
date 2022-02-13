n = int(input())

i = 1

print(i, end=" ")

while True:
    if i * 2 > n:
        break
    print(i * 2, end=" ")
    i *= 2
