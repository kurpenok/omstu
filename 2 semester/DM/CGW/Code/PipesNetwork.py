from copy import deepcopy


class PipesNetwork:
    def __init__(self, nodes: int) -> None:
        self.nodes = nodes
        self.graph = [[float("inf") for _ in range(self.nodes)] for _ in range(self.nodes)]

    def connect(self, u: int, v: int, w: float) -> None:
        self.graph[u][v] = w

    def getMaxValue(self) -> float:
        matrix = deepcopy(self.graph)

        for i in range(self.nodes):
            for u in range(self.nodes):
                for v in range(self.nodes):
                    matrix[u][v] = min([matrix[u][v], matrix[u][i] + matrix[i][v]])

        result = 0
        for line in matrix:
            for element in line:
                if result < element:
                    result = element
        
        return result

