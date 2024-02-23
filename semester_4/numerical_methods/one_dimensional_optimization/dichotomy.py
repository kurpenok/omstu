from typing import Callable


def dichotomy_search(f: Callable, a: float, b: float, eps: float) -> float:
    while abs(a - b) > 2 * eps:
        x = (a + b) / 2
        x_1 = x - (eps / 2)
        x_2 = x + (eps / 2)
        if f(x_1) > f(x_2):
            a = x_1
        else:
            b = x_2

    return f((a + b) / 2)
