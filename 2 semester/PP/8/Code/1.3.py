def changing_the_norm(heights: list) -> int:
    return max(heights) - (sum(heights) // len(heights))


def total(products: list) -> float:
    kcal = 0.0

    for product in products:
        index = 0
        for i, symbol in enumerate(product):
            if symbol.isdigit():
                index = i
                break
        kcal += float(product[index:])

    return kcal


if __name__ == "__main__":
    print(changing_the_norm([150, 160, 164, 147]))
    print(changing_the_norm([170, 162, 156, 153, 159]))
    print(changing_the_norm([158, 168, 172]))

    data = ["Ice cream, strawberry 192",
            "Puff pastry with protein cream 461"]
    print(total(data))

