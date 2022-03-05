status = False
line = 1
for _ in iter(int, 1):
    text = input()
    if not status:
        line += 1
    if text == 'END':
        break
    if 'Star' in text or 'star' in text:
        status = True

if status:
    print(line)
else:
    print('NO')

