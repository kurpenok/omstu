def amount(a: int, b: int) -> int:
    if a == 0:
        return b
    return amount(a - 1, b + 1)


a = int(input())
b = int(input())

print(amount(a, b))
