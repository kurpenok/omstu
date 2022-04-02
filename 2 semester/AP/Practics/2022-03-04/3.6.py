n = int(input())

numbers = [2, 3, 4, 5, 6, 8, 9, 10, 12, 15]

for i in range(16, n + 3):
    for number in numbers[::-1]:
        if i % number in numbers:
            pass

print(numbers[n])

