import math
from typing import Callable

import numpy as np


def grad_f(x: np.ndarray) -> np.ndarray:
    return math.exp(2 - x[0]) * (math.e * (x[0] - 4) + x[1] - 2)


def rosenbrock_search(f: Callable, x_0: np.ndarray, eps: float) -> float:
    x = x_0
    alpha = 0.0001
    grad = grad_f(x_0)

    while abs(grad) > eps:
        x = x - alpha * grad
        grad = grad_f(x)

    return f(x)
