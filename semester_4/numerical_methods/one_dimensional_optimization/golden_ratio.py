from collections.abc import Callable


def golden_ratio_search(f: Callable, a: float, b: float, eps: float) -> float:
    tau = 0.618

    while abs(a - b) < eps:
        x_1 = b - ((b - a) / tau)
        x_2 = a + ((b - a) / tau)
        if f(x_1) >= f(x_2):
            a = x_1
        else:
            b = x_2

    return f((a + b) / 2)
