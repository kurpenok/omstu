a = list(map(int, input().split()))

print(max(a), len(a) - a[::-1].index(max(a)) - 1)
