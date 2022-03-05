status = False

for i in iter(int, 1):
    number = int(input())
    if not number:
        break
    if not status:
        if not (status % 3) and not (status % 7):
            status = True
            print('Ahtung!')
        elif not (number % 3):
            print('Unhappy')
        elif not (number % 7):
            print('Danger')

