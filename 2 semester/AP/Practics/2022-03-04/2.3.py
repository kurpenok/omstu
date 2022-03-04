status = False
index = 1

for _ in iter(int, 1):
    text = input()
    index += 1
    if 'Star' in text or 'star' in text:
        status = index
    elif 'END' in text:
        break

if status:
    print(status)
else:
    print("No")

