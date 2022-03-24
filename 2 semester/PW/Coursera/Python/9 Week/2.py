from sys import stdin


class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = [line.copy() for line in matrix]

    def __add__(self, matrix):
        return Matrix(
            [list(map(sum, zip(*i))) for i in zip(self.matrix, matrix.matrix)])

    def __mul__(self, matrix):
        return Matrix(
            [list(map(lambda x: x * matrix, i)) for i in self.matrix])

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self) -> tuple:
        return len(self.matrix), len(self.matrix[0])

    __rmul__ = __mul__


exec(stdin.read())
