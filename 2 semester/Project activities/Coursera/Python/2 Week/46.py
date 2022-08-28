n1, n2, n3 = int(input()), int(input()), int(input())

c1 = 0
c2 = 0
c3 = 0

while n3 != 0:
    if n1 < n2 > n3:
        c3 += 1
        if c3 == 2:
            c2 = c1
        elif c3 > 2 and c1 < c2:
            c2 = c1
        c1 = 1
    if n1 >= n2 or n3 >= n2:
        c1 += 1
    n1 = n2
    n2 = n3
    n3 = int(input())

print(c2)
