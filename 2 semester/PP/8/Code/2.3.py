def diversity(arg: str) -> int:
    global calls
    calls.append(arg)
    return calls.count(arg)


if __name__ == "__main__":
    calls = []

    print(diversity("Happy"))
    print(diversity("New"))
    print(diversity("Year"))
    print(diversity("Year"))
    print(diversity("Year"))

