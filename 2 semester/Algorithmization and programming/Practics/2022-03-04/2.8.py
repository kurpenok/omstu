from math import ceil

width = int(input("[>] Enter width: "))
count = int(input("[>] Enter count: "))

words = input("[>] Enter words: ").split()

width = ceil(width / 2)

print("[+] Output: ")
for i, word in enumerate(words):
    if (i // width) % 2:
        string = " " * (width - (i % width)) + word
    else:
        string = " " * (i % width) + word
    print(string)

