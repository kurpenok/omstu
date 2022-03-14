with open("input.txt") as data:
    text = data.read().split()

words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

result = [0, ""]

for word in words:
    if result[0] == words[word]:
        result[1] = min(word, result[1])
    elif result[0] < words[word]:
        result[0] = words[word]
        result[1] = word

print(result[1])
