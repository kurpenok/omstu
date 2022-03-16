class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.graph = []

    def addEdge(self, u: int, v: int, w: int) -> None:
        self.graph.append([u, v, w])

    def print(self, dist: list) -> None:
        print("[+] Vertex distance from sourses")
        for i in range(self.vertexes):
            print(f"{i}\t\t{dist[i]}")

    def fordbellman(self, start: int):
        dist = [float("inf")] * self.vertexes
        dist[start] = 0

        for _ in range(self.vertexes - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("[-] The graph has cycles")
                return

        self.print(dist)


if __name__ == "__main__":
    graph = Graph(5)

    graph.addEdge(0, 1, -1)
    graph.addEdge(0, 2, 4)
    graph.addEdge(1, 2, 3)
    graph.addEdge(1, 3, 2)
    graph.addEdge(1, 4, 2)
    graph.addEdge(3, 2, 5)
    graph.addEdge(3, 1, 1)
    graph.addEdge(4, 3, -3)

    graph.fordbellman(0)

