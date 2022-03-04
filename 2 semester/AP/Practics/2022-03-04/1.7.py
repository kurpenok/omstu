from fractions import Fraction

n = input()

s = n.count('santi')
k = n.count('kilo')

result = Fraction(pow(1000, k), pow(100, k))

print(result)

