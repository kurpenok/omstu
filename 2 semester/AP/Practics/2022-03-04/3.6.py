n = int(input())

numbers = [2, 3, 5]

for i in range(n):
    x = numbers.pop(0)
    
    numbers.append(2 * x)
    numbers.append(3 * x)
    numbers.append(5 * x)

    numbers.sort()
    numbers = list(set(numbers))

print(x)

