class Car:
    def __init__(self, color: str, t: str, year: int) -> None:
        self.color = color
        self.type = t
        self.year = year

    def start(self) -> None:
        print("[+] Car was started")

    def mute(self) -> None:
        print("[-] Car was muted")

    def setYear(self, year: int) -> None:
        self.year = year

    def setType(self, t: str) -> None:
        self.type = t

    def setColor(self, color: str) -> None:
        self.color = color


if __name__ == "__main__":
    car = Car("UAZ Patriot", "Auto", 2018)

