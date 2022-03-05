status = False

for _ in iter(int, 1):
    text = input()
    if text == 'END':
        break
    if 'Star' in text or 'star' in text:
        status = True

if status:
    print('YES')
else:
    print('NO')

