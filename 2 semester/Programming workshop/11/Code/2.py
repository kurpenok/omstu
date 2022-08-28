class Contribution:
    def __init__(self, money: int, persent: float, years: int) -> None:
        self.money = money
        self.persent = persent
        self.years = years


class FastContribution(Contribution):
    def __init__(self, money: int, persent: float, years: int) -> None:
        super().__init__(money, persent, years)

    def profit(self) -> float:
        s = self.money

        for _ in range(self.years):
            s += self.money * self.persent

        return s


class BonusContribution(Contribution):
    def __init__(self, money: int, persent: float, years: int) -> None:
        super().__init__(money, persent, years)

    def profit(self) -> float:
        for _ in range(self.years):
            self.money *= (1 + self.persent)

        return self.money


class CapitalPersentsContribution(Contribution):
    def __init__(self, money: int, persent: float, years: int) -> None:
        super().__init__(money, persent, years)

    def profit(self) -> float:
        return 0

