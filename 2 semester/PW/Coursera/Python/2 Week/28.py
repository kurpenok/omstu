from math import log2

n = int(input())

if log2(n).is_integer():
    print("YES")
else:
    print("NO")
