from typing import Callable

import numpy as np


def optimize(f: Callable, i: int, x: np.ndarray, eps: float) -> float:
    x_left = x.copy()
    x_right = x.copy()

    x_left[i] -= eps
    x_right[i] += eps

    while not (f(x_left) > f(x) < f(x_right)):
        if f(x_left) < f(x) < f(x_right):
            x_right, x = x.copy(), x_left.copy()
            x_left[i] -= eps
        elif f(x_left) > f(x) > f(x_right):
            x_left, x = x.copy(), x_right.copy()
            x_right[i] += eps

    return x[i]


def gauss_seidel_search(f: Callable, x_0: np.ndarray, eps: float) -> float:
    for i in range(len(x_0)):
        x_0[i] = optimize(f, i, x_0.copy(), eps)

    return f(x_0)
