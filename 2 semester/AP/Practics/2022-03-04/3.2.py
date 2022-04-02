n = list(map(int, input("[>] Enter numbers: ").split()))
n.sort()

for i in range(3):
    for j in range(3):
        print(f"{n[i]} + {n[j]} = {n[i] + n[j]}", end="\t")
    print()

