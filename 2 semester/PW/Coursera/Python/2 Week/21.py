a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print("INF")
elif c * (-1) * b // a + d == 0:
    print("NO")
elif (-1) * b % a != 0:
    print("NO")
else:
    print((-1) * b // a)
