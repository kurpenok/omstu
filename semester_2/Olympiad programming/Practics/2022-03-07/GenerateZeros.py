def generate(start: int, stop: int, combination: list) -> None:
    if start > stop:
        print(combination)
    else:
        combination.append(0)
        generate(start + 1, stop, combination)
        combination.pop()
        
        combination.append(1)
        generate(start + 1, stop, combination)
        combination.pop()


generate(1, int(input()), [])

