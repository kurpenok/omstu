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

    def floyd(self) -> None:
        matrix = self.graph.copy()

        for i in range(self.vertexes):
            for u in range(self.vertexes):
                for v in range(self.vertexes):
                    matrix[u][v] = min([matrix[u][v], matrix[u][i] + matrix[i][v]])

        self.show(matrix)


graph = Graph(5)

graph.connect(0, 1, -1)
graph.connect(0, 2, 4)
graph.connect(1, 2, 3)
graph.connect(1, 3, 2)
graph.connect(1, 4, 2)
graph.connect(3, 2, 5)
graph.connect(3, 1, 1)
graph.connect(4, 3, -3)

graph.floyd()

