n = int(input())
villages = list(map(int, input().split()))

m = int(input())
shelter_range = input().split()

shelters = []
for i in range(m):
    shelters.append((int(shelter_range[i]), i + 1))
shelters.sort()

for village in villages:
    if village > shelters[-1][0]:
        answer = shelters[-1][1]
    elif village < shelters[0][0]:
        answer = shelters[0][1]
    else:
        low = 0
        high = len(shelters) - 1
        while high - low > 1:
            mid = (low + high) >> 1
            if village > shelters[mid][0]:
                low = mid
            else:
                high = mid

        if village - shelters[low][0] < shelters[high][0] - village:
            answer = shelters[low][1]
        else:
            answer = shelters[high][1]

    print(answer, end=' ')
print()
