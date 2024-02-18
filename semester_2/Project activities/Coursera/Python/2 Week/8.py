n = int(input())
m = int(input())
k = int(input())

if k < m * n and (not (k % m) or not (k % n)):
    print("YES")
else:
    print("NO")
