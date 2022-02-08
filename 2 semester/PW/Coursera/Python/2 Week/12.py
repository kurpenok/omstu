x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

p = y2 - y1
z = abs(x2 - x1)

if 8 < x1 or x1 < 1:
    print("NO")
elif 8 < x2 or x2 < 1:
    print("NO")
elif 8 < y1 or y1 < 1:
    print("NO")
elif 8 < y2 or y2 < 1:
    print("NO")
elif y2 <= y1:
    print("NO")
elif x1 > x2 and x2 < x1 - p:
    print("NO")
elif x2 > x1 and x2 > x1 + p:
    print("NO")
elif p % 2 == 0 and z % 2 == 0:
    print("YES")
elif p % 2 != 0 and z % 2 != 0:
    print("YES")
else:
    print("NO")
