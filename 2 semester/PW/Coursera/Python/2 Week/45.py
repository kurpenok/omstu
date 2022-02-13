numC = numA = numB = int(input())

x = 1
n = 0

while numC != 0:
    if numC > numB > numA or numC < numB < numA:
        x += 1
    elif numC > numB or numC < numB:
        x = 2
    if x > n:
        n = x
    numA = numB
    numB = numC
    numC = int(input())

print(n)
