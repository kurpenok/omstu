n = int(input())

words = {}

for i in range(n):
    synonyms = input().split()
    words[synonyms[0]] = synonyms[1]
    words[synonyms[1]] = synonyms[0]


word = input()

print(words[word])
