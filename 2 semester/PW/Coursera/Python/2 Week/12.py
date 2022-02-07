x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if y2 - y1 >= 0 and (x2 >= y2 - x1 and x2 <= abs(x1 + y1 - 16)):
    print("YES")
else:
    print("NO")
