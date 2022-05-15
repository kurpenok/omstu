def brackets(sequence: str) -> bool:
    brackets_dict = {"]": "[", ")": "(", "}": "{", ">": "<"}

    stack = []

    for symbol in sequence:
        if symbol in "[({<":
            stack.append(symbol)
        elif symbol in "])}>":
            if brackets_dict[symbol] != stack.pop():
                return False
    return True


if __name__ == "__main__":
    print(brackets("[12 / (9) + 2(5{15 * <2 - 3>}6)]"))
    print(brackets("1{2 + [3}45 - 6] * (7 - 8)9"))

