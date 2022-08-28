from collections import defaultdict

n = int(input())

students = defaultdict(list)

languages = set()

for i in range(n):
    count = int(input())
    for j in range(count):
        language = input()
        languages.add(language)
        students[i].append(language)

check = {}
for language in languages:
    check[language] = True

for language in languages:
    for key in list(students.keys()):
        if language not in students[key]:
            check[language] = False
            break

count = 0
for key in list(check.keys()):
    if check[key]:
        count += 1

print(count)
for key in list(check.keys()):
    if check[key]:
        print(key)

print(len(languages))
for language in languages:
    print(language)
