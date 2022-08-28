n = int(input())

for i in range(n):
    for digit in [i for i in range(1, i + 2)]:
        print(digit, end='')
    print()
