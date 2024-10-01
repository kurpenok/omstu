from typing import Callable

import numpy as np
from scipy.optimize import minimize


def conjugate_directions_search(f: Callable, x_0: np.ndarray, eps: float) -> float:
    x = x_0.copy()
    directions = np.eye(len(x_0))

    for _ in range(1000):
        converged = True
        x_new = x.copy()
        for i in range(len(x_0)):
            optimum = minimize(lambda alpha: f(x + alpha * directions[i]), 0)
            x_new = x + optimum.x * directions[i]

            if np.linalg.norm([x_new - x]) > eps:
                converged = False

            x = x_new.copy()

        if converged:
            break

        directions[0] = [x_new - x_0]
        directions[1] = directions[0] * np.array([-1, 1])

    return f(x)
