n = int(input())

n1 = n
c1 = 1
c2 = 1

while n != 0:
    n = int(input())
    if n == n1:
        c1 += 1
        if c1 > c2:
            c2 = c1
    elif n != n1:
        c1 = 1
    n1 = n

print(c2)
