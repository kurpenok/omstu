def reverse() -> None:
    number = int(input())
    if number:
        reverse()
    print(number)


reverse()
