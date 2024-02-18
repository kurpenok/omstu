def degree_indicator(number: float, base: int) -> int:
    count = 0

    if number == 1:
        return 0
    elif number == base:
        return 1
    elif number < 1:
        while number != base**count:
            count -= 1
    elif number > 1:
        while number != base**count:
            count += 1
    return count


def func(number: int) -> int:
    if number == 0:
        return 0
    elif not (number % 3):
        return func(number // 3) + 1
    else:
        return 2 + func(number - 1)


if __name__ == "__main__":
    print(degree_indicator(81, 3))
    print(degree_indicator(1 / 625, 5))
    print(func(6))
    print(func(10000))

