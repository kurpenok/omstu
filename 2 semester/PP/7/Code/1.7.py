def test() -> tuple:
    a = 1
    s = "a"
    return a, s


print(test.__code__.co_nlocals)

