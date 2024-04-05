import numpy as np
import sympy


def phi(x: np.ndarray) -> float:
    return pow(x[0], 2) + 1.5 * x[1] - 2


def f(x: np.ndarray) -> float:
    return x[0] - x[1]


def langrange_multipliers_search() -> None:
    x_1, x_2, w = sympy.symbols("x_1 x_2 w")

    f = x_1 - x_2
    phi = pow(x_1, 2) + 1.5 * x_2 - 2

    g = x_1 - x_2 + w * (pow(x_1, 2) + 1.5 * x_2 - 2)
    gx_1 = g.diff(x_1)
    gx_2 = g.diff(x_2)
    gw = g.diff(w)

    sols = sympy.solve([gx_1, gx_2, gw], x_1, x_2, w)

    print(sols)
