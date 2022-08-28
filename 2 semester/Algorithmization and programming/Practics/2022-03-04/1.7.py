from fractions import Fraction


metre = input()

k = 0
s = 0

for symbol in metre:
    if symbol == 's':
        s += 1
    elif symbol == 'k':
        k += 1

print(Fraction(pow(1000, k) * 100, pow(100, s)))

