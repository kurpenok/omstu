class PearsBasket:
    def __init__(self, n: int) -> None:
        self.n = n

    def __add__(self, other):
        return PearsBasket(self.n + other.n)

    def __sub__(self, other):
        return PearsBasket(self.n - other.n)

    def __mul__(self, other):
        return PearsBasket(self.n * other.n)

    def __floordiv__(self, other):
        return PearsBasket(self.n // other.n)

    def __str__(self) -> str:
        return f"{self.n}"

    def __repr__(self) -> str:
        return f"PearsBasket({self.n})"


class ModularArithmetic:
    def __init__(self, x: int, m: int) -> None:
        self.x = x
        self.m = m
    
    def __call__(self, m) -> int:
        return self.x % m

    def __add__(self, other):
        return ModularArithmetic((self.x + other.x) % self.m, self.m)

    def __sub__(self, other):
        return ModularArithmetic((self.x - other.x) % self.m, self.m)
    
    def __lshift__(self, n):
        return ModularArithmetic((self.x - n) % self.m, self.m)
    
    def __rshift__(self, n):
        return ModularArithmetic((self.x - n) % self.m, self.m)

    def __str__(self) -> str:
        return f"{self.x % self.m}({self.m})"

    def __repr__(self) -> str:
        return f"{self.x % self.m}({self.m})"

