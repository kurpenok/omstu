#!/usr/bin/env python3

import numpy as np

from scipy.linalg import det, lu
from scipy.stats import norm, uniform


def main() -> None:
    a = np.array([
        [1, -4, 2, 1.4],
        [2, -3.5, 9, 0],
        [7, 5, -4, 3],
        [1, 2, 3, 4],
    ])

    print("[+] LU-decomposition:", lu(a))

    print("[+] Determinant:", det(a))

    sample_norm = norm.rvs(size=100)
    print("[+] Normal sample:", sample_norm)

    sample_uniform = uniform.rvs(size=100)
    print("[+] Uniform sample:", sample_uniform)


if __name__ == "__main__":
    main()
