class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.graph = []

    def connect(self, u: int, v: int, w: int) -> None:
        self.graph.append([u, v, w])

    def show(self, distances: list) -> None:
        print(distances)

    def fordbellman(self, start: int) -> None:
        d = [float("inf") for _ in range(self.vertexes)]
        d[start] = 0

        for _ in range(self.vertexes - 1):
            for u, v, w in self.graph:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w

        self.show(d)


graph = Graph(5)

graph.connect(0, 1, -1)
graph.connect(0, 2, 4)
graph.connect(1, 2, 3)
graph.connect(1, 3, 2)
graph.connect(1, 4, 2)
graph.connect(3, 2, 5)
graph.connect(3, 1, 1)
graph.connect(4, 3, -3)

graph.fordbellman(0)

