m = float("-inf")

while True:
    n = int(input())
    if not n:
        print(m)
        break
    elif m < n:
        m = n
