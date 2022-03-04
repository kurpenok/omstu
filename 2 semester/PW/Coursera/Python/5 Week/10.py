a = list(map(int, input().split()))
b = []

for e in a:
    if e > 0:
        b.append(e)

print(min(b))
