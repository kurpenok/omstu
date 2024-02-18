def get_min(graph: list, unified: set):
    rm = (float("inf"), -1, -1)

    for top in unified:
        rr = min(graph, key=lambda x: x[0] if (x[1] == top or x[2] == top) and (x[1] not in unified or x[2] not in unified) else float("inf"))
        if rm[0] > rr[0]:
            rm = rr
    
    return rm


count = int(input("[>] Enter count of tops: "))

graph = [(float("inf"), -1, -1)]

status = True

while True:
    status = input("[>] Enter the element of graph (lenght, top 1, top 2): ")
    if status:
        status = tuple(map(int, status.split()))
        graph.append(status)
    else:
        break

unified = {1}
skeleton = []

while len(unified) < count:
    r = get_min(graph, unified)
    if r[0] == float("inf"):
        break
    
    skeleton.append(r)
    unified.add(r[1])
    unified.add(r[2])

print(skeleton)

