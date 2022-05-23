class Quadratic:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

        self.d = self.b**2 - 4 * self.a * self.c
        
        self.solution = []

        if self.d < 0:
            self.solution.append(None)
        elif self.d == 0:
            self.solution.append(-self.b / (2 * self.a))
        else:
            self.solution.append((-self.b + self.d**0.5) / (2 * self.a))
            self.solution.append((-self.b - self.d**0.5) / (2 * self.a))

    def branch(self) -> str:
        if self.a < 0:
            return "dowm"
        else:
            return "up"

    def sections(self) -> tuple:
        return tuple(self.solution)

    def top(self) -> tuple:
        x = -self.b / (2 * self.a)
        y = self.a * x * x + self.b * x + self.c
        return x, y

    def x_sect(self) -> int:
        if self.solution[0] is None:
            return 0
        elif len(self.solution) == 1:
            return 1
        else:
            return 2

    def y_sect(self) -> tuple:
        return 0, self.c


if __name__ == "__main__":
    quadratic = Quadratic(1, -6, 9)
    print(quadratic.x_sect())
    print(quadratic.branch())
    print(quadratic.top())
    print(quadratic.y_sect())
    print(quadratic.sections())

