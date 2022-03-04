def min4(a: int, b: int, c: int, d: int) -> int:
    return min(min(a, b), min(c, d))


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
