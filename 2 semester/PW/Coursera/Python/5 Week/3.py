n = int(input())

for i in range(n):
    print('+___', end=' ')
print()

for i in range(n):
    print(f'|{i + 1} /', end=' ')
print()

for i in range(n):
    print('|__\\', end=' ')
print()

for i in range(n):
    print('|   ', end=' ')
print()
