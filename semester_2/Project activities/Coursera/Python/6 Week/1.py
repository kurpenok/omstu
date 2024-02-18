def merge(a: list, b: list):
    c = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:]
    c += b[j:]

    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
