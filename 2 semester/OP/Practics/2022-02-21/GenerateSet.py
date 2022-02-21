def generate(start: int, stop: int, subsets: list) -> None:
    if start > stop:
        print(subsets)
    else:
        subsets.append(start)
        generate(start + 1, stop, subsets)

        subsets.pop()
        generate(start + 1, stop, subsets)


n = int(input())

subsets = list()

generate(1, n, subsets)

