n = int(input())

names = ''

for i in range(n):
    name = input()
    names += f'{i + 1} {name}\n'

print(names)

