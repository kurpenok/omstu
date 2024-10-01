import math
from typing import Callable

import numpy as np


def f(x: np.ndarray) -> float:
    A = 20
    a = 3
    b = 2
    return A - ((x[0] - a) * math.exp(-x[0] + a)) - ((x[1] - b) * math.exp(-x[1] + b))


def grad_f(x: np.ndarray) -> np.ndarray:
    return math.exp(2 - x[0]) * (math.e * (x[0] - 4) + x[1] - 2)


def line_search(x: np.ndarray, d: np.ndarray) -> float:
    alpha = 0.1
    while f(x + alpha * d) > f(x):
        alpha *= 0.5
    return alpha


def steepest_descent_search(f: Callable, x_0: np.ndarray, eps: float) -> float:
    x = x_0.copy()

    for _ in range(1000):
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps:
            break
        d = -grad
        alpha = line_search(x, d)
        x += alpha * d

    return f(x)
