with open("input.txt") as data:
    text = data.read().split()

words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(*sorted(words, key=lambda x: (-words[x], x)), sep="\n")
