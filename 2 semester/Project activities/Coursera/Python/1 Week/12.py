a = int(input())
b = int(input())
n = int(input())

s = (a * 100) + b

s *= n

a = s // 100
b = s % 100

print(a, b)
