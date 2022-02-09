def bubble(tops: list) -> None:
    def swap(i, j):
        tops[i], tops[j] = tops[j], tops[i]
    
    n = len(tops)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n - x):
            if tops[i - 1][0] > tops[i][0]:
                swap(i - 1, i)
                swapped = True


count = int(input("[>] Enter count of tops: "))

graph = [(float("inf"), -1, -1)]

status = True

while True:
    status = input("[>] Enter ti element of graph (lenght, top 1, top 2): ")
    if status:
        status = tuple(map(int, status.split()))
        graph.append(status)
    else:
        break

print()
print("[+] Before:", graph)

bubble(graph)

print()
print("[+] After:", graph)

skeleton = list()
unified = list()

for top in graph:
    if top[0] == float("inf"):
        break

    if top[1] not in unified or top[2] not in unified:
        skeleton.append(top)
        unified.append(top[1])
        unified.append(top[2])

    count += 1

print()
print("[+] Skeleton:", skeleton)

