class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.graph = []

    def connect(self, u: int, v: int, w: int) -> None:
        self.graph.append([u, v, w])

    def print(self, distances: int) -> None:
        pass

    def fordbellman(self, start: int) -> None:
        pass

