def count(s: str) -> int:
    count = 0
    for symbol in s:
        if symbol in "aeyuoi":
            count += 1
    return count


text = input().split()

amount = 0

for word in text:
    amount += count(word) - 1

print(amount)

