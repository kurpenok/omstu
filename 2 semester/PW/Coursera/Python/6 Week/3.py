s, n = map(int, input().split())

a = []

for i in range(n):
    size = int(input())
    a.append(size)

a.sort()

users = 0
size = 0

for user in a:
    if size + user > s:
        break
    size += user
    users += 1

print(users)
