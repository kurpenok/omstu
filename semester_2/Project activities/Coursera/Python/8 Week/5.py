from functools import reduce

print(reduce(lambda m, x: m * x**5, map(int, input().split()), 1))
