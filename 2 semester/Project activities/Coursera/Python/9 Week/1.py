from sys import stdin


class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = [line.copy() for line in matrix]

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self) -> tuple:
        return len(self.matrix), len(self.matrix[0])


exec(stdin.read())
