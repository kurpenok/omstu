with open("input.txt") as data:
    text = data.read().split()

words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 0
    print(words[word], end=" ")

print()
