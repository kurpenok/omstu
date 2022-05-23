from math import factorial


class Student:
    def __init__(self, name: str, university: str) -> None:
        self.name = name
        self.university = university
        self.year = 1

    def getName(self) -> str:
        return self.name

    def getUniversity(self) -> str:
        return self.university

    def getYear(self) -> int:
        return self.year
    
    def study(self) -> None:
        if self.year < 6:
            self.year += 1


class Employee:
    def __init__(self, name: str, company: str) -> None:
        self.positions = ["junior", "middle", "senior", "lead"]

        self.name = name
        self.company = company
        self.status = (0, self.positions[0])

    def getName(self) -> str:
        return self.name

    def getCompany(self) -> str:
        return self.company

    def getPosition(self) -> str:
        return self.status[1]

    def work(self) -> None:
        if self.status[0] < 4:
            self.status = (self.status[0] + 1, self.positions[self.status[0] + 1])


class EulerNumber:
    def __init__(self, n: int) -> None:
        self.n = n

        self.e = 1

        for i in range(1, n):
            self.e += i / factorial(i)

    def getNumber(self, x=1) -> float:
        return self.e**x

