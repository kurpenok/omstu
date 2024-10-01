import numpy as np
import sympy


def langrange_multipliers_search() -> np.ndarray:
    x_1, x_2, w = sympy.symbols("x_1 x_2 w")

    f = x_1 - x_2
    g = pow(x_1, 2) + 1.5 * pow(x_2, 2) - 2
    l = f - w * g

    dl_dx_1 = l.diff(x_1)
    dl_dx_2 = l.diff(x_2)
    dl_dw = l.diff(w)

    solutions = sympy.solve([dl_dx_1, dl_dx_2, dl_dw], x_1, x_2, w)

    return solutions
