n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))
b.sort()

indexes = {}

for i in range(len(b)):
    indexes[i + 1] = b[i]

c = []

for peoples in a:
    delta_1 = (float("inf"), 0)
    delta_2 = float("inf")

    for saves in b:
        if abs(saves - peoples) < delta_1[0]:
            delta_2 = delta_1[0]
            delta_1 = (abs(saves - peoples), saves)
        elif abs(saves - peoples) > delta_1[0] and delta_2 < delta_1[0]:
            break
    
    print(indexes.values())

