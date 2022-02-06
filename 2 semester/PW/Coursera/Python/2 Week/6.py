x = int(input())
y = int(input())

if x - 1 >= y - x + 1 and not (x - 1 % y - x + 1):
    print("YES")
else:
    print("NO")
