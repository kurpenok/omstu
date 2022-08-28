a = list(map(int, input().split()))

d = {}

for e in a:
    if e in d:
        print("YES")
    else:
        d[e] = 1
        print("NO")
