a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = list(sorted(a.intersection(b)))

print(*c)
