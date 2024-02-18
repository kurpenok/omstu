start = int(input())
step = int(input())
stop = int(input())

for height in range(start, stop - step + 1, -step):
    print(f'[+] Height: {height}')

print('[+] Glissade')

