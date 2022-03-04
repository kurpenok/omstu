for _ in iter(int, 1):
    n = int(input())
    if not (n % 3) and not (n % 7):
        print('[-] Ahtung!')
        break
    elif not (n % 3):
        print('[-] Unhappy')
    elif not (n % 7):
        print('[-] Danger')
    else:
        print(n)

