def status(data: list) -> str:
    lines = []

    for line in data:
        c = 0
        t = 0
        for vegetable in line:
            if "0" in str(vegetable):
                c += 1
            else:
                t += 1
        lines.append(1 if c <= t else 0)

    if all(lines):
        return "EVERGREEN TOMATOES"
    return "ALUMINIUM CUCUMBERS"


if __name__ == "__main__":
    print(status([
            [1, 3, 6, 20],
            [2, 2, 10, 70, 50],
            [20, 10, 1]
        ]))

    print(status([
            [6, 20, 7, 103],
            [17],
            [1, 402, 14],
            [18, 3, 201, 909]
        ]))

