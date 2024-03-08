from typing import Callable


def optimize(f: Callable, i: int, x: list[float], eps: float) -> float:
    x_left = x[:]
    x_right = x[:]

    x_left[i] -= eps
    x_right[i] += eps

    while not (f(x_left) > f(x) < f(x_right)):
        if f(x_left) < f(x) < f(x_right):
            x_right, x = x[:], x_left[:]
            x_left[i] -= eps
        elif f(x_left) > f(x) > f(x_right):
            x_left, x = x[:], x_right[:]
            x_right[i] += eps

    return x[i]


def gauss_seidel_search(f: Callable, x_0: list[float], eps: float) -> float:
    for i in range(len(x_0)):
        x_0[i] = optimize(f, i, x_0, eps)

    return f(x_0)
