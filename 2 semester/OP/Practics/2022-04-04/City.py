from copy import deepcopy


class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.graph = [[float("inf") for _ in range(self.vertexes)] for _ in range(self.vertexes)]

    def connect(self, u: int, v: int, w: int) -> None:
        self.graph[u][v] = w

    def show(self, matrix: list) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(f"{matrix[i][j]}", end=" ")
            print()

    def floyd(self) -> list:
        matrix = deepcopy(self.graph)

        for i in range(self.vertexes):
            for u in range(self.vertexes):
                for v in range(self.vertexes):
                    matrix[u][v] = min([matrix[u][v], matrix[u][i] + matrix[i][v]])

        return matrix


n, m = map(int, input().split())

graph = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph.connect(u, v, w)

matrix = graph.floyd()

paths = []
for line in matrix:
    paths.append(min(line))

print(max(paths))

