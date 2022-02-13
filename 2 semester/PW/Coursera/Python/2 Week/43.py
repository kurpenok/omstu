z = int(input())

n = 1
j = 0

while n <= z:
    k = 0
    i = 0
    m = n

    while m != 0:
        m //= 10
        k += 1
    while i < k:
        m += 10**(k - i - 1) * ((n // 10**i) % 10)
        i += 1
    if n == m:
        j += 1
    n += 1

print(j)
