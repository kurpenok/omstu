a = list(map(int, input().split()))

for i in range(1, len(a) - 1, 2):
    print(a[i], a[i - 1], end=' ')

if len(a) % 2:
    print(a[-1])
else:
    print(a[-1], a[-2])
