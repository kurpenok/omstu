from math import sqrt


def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())
p1, p2 = map(int, input().split())

d1 = get_distance(x1, x2, y1, y2)
d2 = get_distance(x1, x2, z1, z2)
d3 = get_distance(x1, x2, p1, p2)
d4 = get_distance(y1, y2, z1, z2)
d5 = get_distance(y1, y2, p1, p2)
d6 = get_distance(z1, z2, p1, p2)

print(max([d1, d2, d3, d4, d5, d6]))

