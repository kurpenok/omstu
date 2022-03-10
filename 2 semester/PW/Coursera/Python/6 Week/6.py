def CountSort(a: list) -> list:
    new_a = [0] * 101
    for i in a:
        new_a[i] += 1

    sort_a = []
    for i in range(len(new_a)):
        sort_a.extend([i] * new_a[i])

    return sort_a


a = list(map(int, input().split()))

print(*CountSort(a))
