def get_max(a: int, b: int, c: int) -> int:
    if a < b:
        if b < c:
            return c
        else:
            return b
    elif b < c:
        if c < a:
            return a
        else:
            return c
    elif a < c:
        if c < b:
            return b
        else:
            return c
    else:
        return -1

