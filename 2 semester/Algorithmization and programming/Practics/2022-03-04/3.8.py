n = int(input())

mods = []

while n > 1:
    for i in range(2, n + 1):
        if not (n % i):
            mods.append(i)
            n //= i
            break

print(*mods)

