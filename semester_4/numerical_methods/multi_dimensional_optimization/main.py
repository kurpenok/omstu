import math

import numpy as np

from conjugate_directions import conjugate_directions_search
from gauss_seidel import gauss_seidel_search


def f(x: np.ndarray) -> float:
    A = 20
    a = 3
    b = 2
    return A - ((x[0] - a) * math.exp(-x[0] + a)) - ((x[1] - b) * math.exp(-x[1] + b))


def main() -> None:
    x_0 = np.zeros(2)
    eps = 0.0001

    print(f"[+] Gauss-Seidel: {gauss_seidel_search(f, x_0, eps):.2f}")
    print(f"[+] Conjugate directions: {conjugate_directions_search(f, x_0, eps):.2f}")


if __name__ == "__main__":
    main()
