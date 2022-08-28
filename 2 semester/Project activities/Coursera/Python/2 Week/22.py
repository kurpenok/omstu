k = int(input())
m = int(input())
n = int(input())

a = n * 2

if n <= k:
    print(m * 2)
elif not (a % k):
    print(a // k * m)
elif a % k:
    print(a // k * m + m)
