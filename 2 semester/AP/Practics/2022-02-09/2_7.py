homes = list(map(int, input("[>] Enter height of homes: ").split()))

index = 1

while index < len(homes):
    if not index:
        print(index + 1)
    if homes[index] >= homes[index - 1]:
        i = 0
        s = True
        while i < index:
            if homes[i] <= homes[i - 1]:
                s = False
                break
        if s:
            print(index + 1)
 
