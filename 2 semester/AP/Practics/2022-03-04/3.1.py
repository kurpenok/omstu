n = int(input())

count = 1

for i in range(n):
    for j in range(n):
        print(count, end="\t")
        count += 1
    print()

