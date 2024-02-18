n = int(input())

mod = 2

while True:
    if not (n % mod):
        print(mod)
        break
    mod += 1
