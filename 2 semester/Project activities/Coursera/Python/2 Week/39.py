sequence = []

while True:
    n = int(input())
    if n:
        sequence.append(n)
    else:
        break

print(sequence.count(max(sequence)))
