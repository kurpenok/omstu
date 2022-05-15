def horse(start: str, stop: str) -> bool:
    words = "abcdefgh"

    symbol = words.find(start[0])
    digit = int(start[1])

    motions = []

    if 0 < symbol - 2 and digit + 1 <= 8:
        motions.append(f"{words[symbol - 2]}{digit + 1}")
    if 0 < symbol - 1 and digit + 2 <= 8:
        motions.append(f"{words[symbol - 1]}{digit + 2}")
    if symbol + 1 <= 8 and digit + 2 <= 8:
        motions.append(f"{words[symbol + 1]}{digit + 2}")
    if symbol + 2 <= 8 and digit + 1 <= 8:
        motions.append(f"{words[symbol + 2]}{digit + 1}")
    if symbol + 2 <= 8 and 0 < digit - 1:
        motions.append(f"{words[symbol + 2]}{digit - 1}")
    if symbol + 2 <= 8 and 0 < digit - 2:
        motions.append(f"{words[symbol + 2]}{digit - 2}")
    if 0 < symbol - 1 and 0 < digit - 2:
        motions.append(f"{words[symbol - 1]}{digit - 2}")
    if 0 < symbol - 2 and 0 < digit - 1:
        motions.append(f"{words[symbol - 2]}{digit - 1}")

    return stop in motions


if __name__ == "__main__":
    print(horse("d4", "b3"))
    print(horse("d4", "a3"))

