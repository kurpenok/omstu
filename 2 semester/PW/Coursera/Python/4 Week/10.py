def amount(s: int):
    number = int(input())
    if number:
        return amount(s + number)
    return s


print(amount(0))
