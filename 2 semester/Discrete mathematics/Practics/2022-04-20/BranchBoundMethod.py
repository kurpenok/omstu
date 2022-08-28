class Graph:
    def __init__(self, vertexes) -> None:
        self.vertexes = vertexes
        self.graph = []

    def connect(self, u: int, v: int, w: int) -> None:
        self.graph.append([u, v, w])

    def branch_bound(self) -> tuple:
        path = []
        lenght = 0

        return path, lenght


graph = Graph(5)

graph.connect(0, 1, 10)

path, lenght = graph.branch_bound()
print(f"[+] Path: {path}")
print(f"[+] Lenght: {lenght}")

