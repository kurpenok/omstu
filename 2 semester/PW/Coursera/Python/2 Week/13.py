a = int(input())
b = int(input())
c = int(input())

cosC = (a**2 + b**2 - c**2) / (2 * a * b)
cosB = (a**2 + c**2 - b**2) / (2 * a * c)
cosA = (b**2 + c**2 - a**2) / (2 * b * c)

if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("rectangular")
elif a + b > c and a + c > b and b + c > a:
    if cosA < 0 or cosB < 0 or cosC < 0:
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
