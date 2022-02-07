x = int(input())
y = int(input())

if (2 * y + 1 - x) % (y - x + 1) == 0:
    print("YES")
else:
    print("NO")
