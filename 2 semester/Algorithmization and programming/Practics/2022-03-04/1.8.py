text = input().split()

vowels = 'aeyuio'
count = 0

for word in text:
    for symbol in word:
        if symbol in vowels:
            count += 1
    count -= 1

print(count)

