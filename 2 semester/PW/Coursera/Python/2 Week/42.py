A = int(input())
B = int(input())

while A != B:
    if A % 2 == 0 and A // 2 >= B:
        A = A // 2
        print(":2")
    elif A % 2 == 0 and A // 2 < B:
        A -= 1
        print("-1")
    elif A % 2 != 0:
        A -= 1
        print("-1")
