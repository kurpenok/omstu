import sys

text = ""

while True:
    line = sys.stdin.readline()
    if not line:
        break
    text += line

words = set(text.split())

print(len(words))
