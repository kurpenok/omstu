from random import randint

a = [randint(-20, 30) for _ in range(10)]
b = [i for i in range(-10, 11, 2)]

for i in a:
    if i % 2:
        b.append(i)

c = []
for i in a:
    if i % 2:
        c.append(i)



print(f"[+] Array A: {a}")
print(f"[+] Array A: {b}")

