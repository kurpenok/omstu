previous = ''

kind = 0
angry = 0

for i in iter(int, 1):
    request = input()
    if request == 'what':
        if kind > angry and previous == 'kind':
            print('Argentum')
        elif kind < angry and previous == 'angry':
            print('Aurum')
        else:
            print('Go fucking back!')
            break
    previous = request
    if request == 'kind':
        kind += 1
    elif request == 'angry':
        angry += 1

