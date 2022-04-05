from random import randint

n = int(input("[>] Enter number: "))

a = [randint(-5, 5) for _ in range(n)]
a_copy = a.copy()

print(f"[+] Array: {a}")

for i in range(n):
    a_copy[i] = abs(a_copy[i])

max_1 = max(a_copy)
a_copy.remove(max_1)
max_2 = max(a_copy)
a_copy.append(max_1)

print(f"[+] First maximum: {max_1}")
print(f"[+] Second maximum: {max_2}")

s = 0
for i in a_copy:
    if i < 1:
        s += i

print(f"[+] Sum of numbers less than one: {s}")

for i in range(n):
    if abs(a[i]) > max(a):
        a[i] = 0

a.sort()

zeros_count = a.count(0)

if zeros_count:
    a = a[:a.index(0)] + a[:zeros_count] + [0] * zeros_count

print(f"[+] Result: {a}")

