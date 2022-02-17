def find_lowest_cost_node(costs: dict, processed: list) -> str:
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


graph = {}

graph["start"] = {}
graph["start"]["a"] = 53
graph["start"]["b"] = 87
graph["start"]["c"] = 15

graph["a"] = {}
graph["a"]["b"] = 15
graph["a"]["c"] = 44
graph["a"]["d"] = 22
graph["a"]["fin"] = 72

graph["b"] = {}
graph["b"]["c"] = 31
graph["b"]["d"] = 17
graph["b"]["fin"] = 14

graph["c"] = {}
graph["c"]["fin"] = 84

graph["d"] = {}
graph["d"]["c"] = 16

graph["fin"] = {}

costs = {}
costs["a"] = 53
costs["b"] = 87
costs["c"] = 15
costs["fin"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["fin"] = None

processed = []

node = find_lowest_cost_node(costs, processed)

while node is not None:
    cost = costs[node]
    neightbors = graph[node]
    for n in neightbors.keys():
        new_cost = cost + neightbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)

print(costs["fin"])

