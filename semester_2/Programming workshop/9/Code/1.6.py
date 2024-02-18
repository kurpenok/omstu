def save_numbers(enter: list) -> list:
    numbers = []

    for word in enter:
        if word.isdigit() and int(word) :
            numbers.append(word)

    return numbers


if __name__ == "__main__":
    print(save_numbers("sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5".split()))

