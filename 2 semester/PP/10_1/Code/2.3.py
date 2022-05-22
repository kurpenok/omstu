class Math:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def addition(self) -> float:
        return self.a + self.b

    def subtraction(self) -> float:
        return self.a - self.b

    def multiplication(self) -> float:
        return self.a * self.b

    def division(self) -> float:
        return self.a / self.b


if __name__ == "__main__":
    math = Math(8, 2)

    print(math.addition())
    print(math.subtraction())
    print(math.multiplication())
    print(math.division())

