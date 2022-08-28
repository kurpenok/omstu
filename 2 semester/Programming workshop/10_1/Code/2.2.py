class Student:
    def __init__(self, name="Ivan", group="10a", age=18) -> None:
        self.name = name
        self.group = group
        self.age = age

    def getName(self) -> str:
        return self.name

    def getGroup(self) -> str:
        return self.group

    def getAge(self) -> int:
        return self.age

    def setName(self, name: str) -> None:
        self.name = name

    def setGroup(self, group: str) -> None:
        self.group = group

    def setAge(self, age: int) -> None:
        self.age = age


if __name__ == "__main__":
    student_1 = Student("Kuat", "FIT-212", 18)
    student_2 = Student("Alexey", "FIT-212", 18)
    student_3 = Student("Vladimir", "FIT-212", 18)
    student_4 = Student("Ivan", "FIT-212", 18)
    student_5 = Student("Artyom", "IVT-211", 18)

