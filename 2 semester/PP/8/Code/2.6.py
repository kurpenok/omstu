def quarters(data: list) -> tuple:
    output = []

    for point in data:
        if point[0] > 0 and point[1] > 0:
            output.append(1)
        elif point[0] > 0 and point[1] < 0:
            output.append(4)
        elif point[0] < 0 and point[1] > 0:
            output.append(2)
        elif point[0] < 0 and point[1] < 0:
            output.append(3)

    return output.count(1), output.count(2),\
            output.count(3), output.count(4)


if __name__ == "__main__":
    print(quarters([(1, 1), (-1, 2), (-3, -1)]))
    print(quarters([(-5, 1), (-1, 3), (2, -1), (0, 3)]))

