from collections import defaultdict

class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.graph = defaultdict(set)
        self.visited = list() 

    def connect(self, u: int, v: int) -> None:
        self.graph[u].add(v)

    def dfs(self, start: int, visited=None) -> set:
        if visited is None:
            visited = set()
        visited.add(start)
        self.visited.append(start)
        for n in self.graph[start] - visited:
            self.dfs(n, visited)
        return visited

    def find_connectivity_components(self) -> int:
        components = 1
        for i in range(self.vertexes):
            self.visited = list(set(self.visited))
            if not self.visited[i]:
                self.dfs(i)
                components += 1
        return components


graph = Graph(5)

graph.connect(0, 1)
graph.connect(0, 2)
graph.connect(1, 2)
graph.connect(1, 3)
graph.connect(1, 4)
graph.connect(3, 2)
graph.connect(3, 1)
graph.connect(4, 3)

graph.find_connectivity_components()

