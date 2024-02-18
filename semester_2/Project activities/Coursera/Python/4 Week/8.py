def power(a: float, n: int) -> float:
    if n == 0:
        return 1
    if n % 2:
        return a * power(a, n - 1)
    return (a**2)**(n // 2)


a = float(input())
n = int(input())

print(power(a, n))
