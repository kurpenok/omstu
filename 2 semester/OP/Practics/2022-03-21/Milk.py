n = int(input())

primary = (0, float("inf"))

for i in range(n):
    x1, y1, z1, x2, y2, z2, c1, c2 = map(float, input().split())

    s1 = 2 * (x1 * y1 + y1 * z1 + x1 * z1)
    s2 = 2 * (x2 * y2 + y2 * z2 + x2 * z2)

    v1 = x1 * y1 * z1 * 0.001
    v2 = x2 * y2 * z2 * 0.001
    
    # System of linear equations
    # c1 = a * s1 + b * v1
    # c2 = a * s2 + b * v2

    det = s1 * v2 - s2 * v1
    det1 = c1 * v2 - c2 * v1
    det2 = s1 * c2 - s2 * c1

    box = det1 / det
    milk = det2 / det

    if milk < primary[1]:
        primary = (i + 1, milk)


print(primary[0], round(primary[1], 2))

