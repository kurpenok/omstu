a = list(map(int, input().split()))

for i in range(len(a)):
    if not (a[i] % 2):
        print(a[i])
