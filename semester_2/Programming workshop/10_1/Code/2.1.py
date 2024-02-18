class ToyClass:
    def __init__(self, p1: float, p2: list, p3: str) -> None:
        self.parameter_1 = p1
        self.parameter_2 = p2
        self.parameter_3 = p3

    def show(self) -> None:
        print(self.parameter_1)
        print(self.parameter_2)
        print(self.parameter_3)

    def instance_method(self) -> str:
        return f"[+] Instance method called: {self}"

    @classmethod
    def class_method(cls) -> str:
        return f"[+] Class method called: {cls}"

    @staticmethod
    def static_method():
        return f"[+] Static method called"


if __name__ == "__main__":
    toy = ToyClass(3.1415926, ["List"], "String")
    toy.show()

