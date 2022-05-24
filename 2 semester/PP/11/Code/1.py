class Pizza:
    def __init__(self, name: str, dough: str, sauce: str, filling: list, cost: float) -> None:
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} from {self.dough} with {self.sauce} and {self.filling}: {self.cost}"

    def prepare(self) -> str:
        return f"[+] Preparing"

    def bake(self) -> str:
        return f"[+] Baking"

    def cut(self) -> str:
        return f"[+] Cutting"

    def pack(self) -> str:
        return f"[+] Packing"


class Pepperoni(Pizza):
    def __init__(self, name: str, dough: str, sauce: str, filling: list, cost: float) -> None:
        super().__init__(name, dough, sauce, filling, cost)


class Barbecue(Pizza):
    def __init__(self, name: str, dough: str, sauce: str, filling: list, cost: float) -> None:
        super().__init__(name, dough, sauce, filling, cost)


class SeaGifts(Pizza):
    def __init__(self, name: str, dough: str, sauce: str, filling: list, cost: float) -> None:
        super().__init__(name, dough, sauce, filling, cost)


class Order:
    def __init__(self, orders: list) -> None:
        self.orders = orders
        self.count = len(orders)

    def __str__(self) -> str:
        return f"[+] Orders: {self.orders}"

    def add(self, pizza: Pizza) -> None:
        self.orders.append(pizza)
        self.count += 1

    def sum(self) -> float:
        result = 0

        for order in self.orders:
            result += order.cost

        return result

    def perform(self) -> None:
        pass


class Terminal:
    def __init__(self, menu: list, order: Order, show: bool) -> None:
        self.menu = menu
        self.order = order
        self.show = show

    def __str__(self) -> str:
        return f"[+] Order: {self.order}"

    def showMenu(self) -> str:
        result = ""

        for element in self.menu:
            result += f"{element}\n"

        return result

    def command(self) -> str:
        return f"[+] Command is done"

    def acceptPayment(self) -> str:
        return f"[+] Payment is accepted"

