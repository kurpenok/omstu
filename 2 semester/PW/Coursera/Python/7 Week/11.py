with open("input.txt", "r", encoding="utf-8") as data:
    text = data.readlines()

presidents = {}

for president in text:
    if president in presidents:
        presidents[president] += 1
    else:
        presidents[president] = 1

p = sorted(presidents, key=lambda x: (-presidents[x], x))

if presidents[p[0]] > len(text) / 2:
    with open("output.txt", "w", encoding="utf-8") as data:
        data.write(p[0])
else:
    with open("output.txt", "w", encoding="utf-8") as data:
        data.write(p[0])
        data.write(p[1])
