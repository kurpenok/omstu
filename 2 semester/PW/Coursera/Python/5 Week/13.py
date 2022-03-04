a = list(map(int, input().split()))

index_min = a.index(min(a))
index_max = a.index(max(a))

for i in range(len(a)):
    if i == index_min:
        print(a[index_max])
    elif i == index_max:
        print(a[index_min])
    else:
        print(a[i])
