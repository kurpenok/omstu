from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.vertexes = set()
        self.weights = dict()
        self.edges = defaultdict(list)

    def addVertex(self, vertex: str) -> None:
        self.vertexes.add(vertex)

    def addEdge(self, u: str, v: str, weight: int) -> None:
        self.edges[u].append(v)
        self.weights[(u, v)] = weight

    def dijkstra(self, start: str) -> None:
        visited = {start: 0}
        path = defaultdict(list)

        vertexes = self.vertexes

        while vertexes:
            minimal = None
            for vertex in vertexes:
                if vertex in visited:
                    if minimal is None:
                        minimal = vertex
                    elif visited[vertex] < visited[minimal]:
                        minimal = vertex
            if minimal is None:
                break

            vertexes.remove(minimal)
            current_weight = visited[minimal]

            for edge in self.edges[minimal]:
                weight = current_weight + self.weights[(minimal, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minimal)

        print("[+] Dijkstra result (visited vertexes): ", visited)
        print("[+] Dijkstra result (full path): ", path)


if __name__ == "__main__":
    graph = Graph()

    graph.addVertex("a")
    graph.addVertex("b")
    graph.addVertex("c")
    graph.addVertex("d")
    graph.addVertex("e")
    graph.addVertex("f")

    graph.addEdge("a", "b", 2)
    graph.addEdge("a", "c", 5)
    graph.addEdge("b", "c", 6)
    graph.addEdge("b", "d", 1)
    graph.addEdge("b", "e", 3)
    graph.addEdge("c", "f", 8)
    graph.addEdge("d", "e", 4)
    graph.addEdge("e", "f", 7)

    graph.dijkstra("a")

