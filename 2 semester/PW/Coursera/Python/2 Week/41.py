A = int(input())

n = 1
a = 0
b = 1
c = a + b

while c < A:
    c = a + b
    a, b = b, c
    n += 1

if A == 0:
    print(0)
elif A != c:
    print(-1)
else:
    print(n)
