from collections.abc import Callable


def fibonacci(n: int) -> int:
    x = 1
    y = 1
    for _ in range(2, n):
        y = x + y
        x = y - x
    return y


def fibonacci_search(f: Callable, a: float, b: float, eps: float) -> float:
    n = 100
    x_1 = a + (b - a) * (fibonacci(n - 2) / fibonacci(n))
    x_2 = b - (b - a) * (fibonacci(n - 1) / fibonacci(n))

    while n > 1:
        if abs(x_1 - x_2) < eps:
            break

        if f(x_1) > f(x_2):
            a = x_1
            x_1 = x_2
            x_2 = b - (x_1 - a)
        else:
            b = x_2
            x_2 = x_1
            x_1 = a + (b - x_2)

        n -= 1

    return f((x_1 + x_2) / 2)
