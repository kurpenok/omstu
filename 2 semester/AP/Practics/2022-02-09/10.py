homes = list(map(int, input().split("\n")))

index = 1

while start < len(homes):
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
    
