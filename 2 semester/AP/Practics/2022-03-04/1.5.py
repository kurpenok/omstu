symbol = input()
n = int(input())

count = 0

for i in range(n):
    if input() == symbol:
        count += 1

print(count)

