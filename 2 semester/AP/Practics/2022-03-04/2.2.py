status = False

for _ in iter(int, 1):
    text = input()
    if 'Star' in text or 'star' in text:
        status = True
    elif 'END' in text:
        break

if status:
    print("Go")
else:
    print("No")

