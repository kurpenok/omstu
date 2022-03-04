n = int(input())
a = list(map(int, input().split()))
x = int(input())

delta = float("inf")
eps = 0

for e in a:
    if abs(x - e) < delta:
        eps = e
        delta = abs(x - e)

print(eps)
