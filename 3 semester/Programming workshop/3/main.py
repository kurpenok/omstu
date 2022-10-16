#!/usr/bin/env python3

import numpy as np
import scipy

from scipy.linalg import det, lu
from scipy.stats import chisquare, norm, uniform


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

    print("[+] Mean of NS:", np.mean(sample_norm))
    print("[+] Mode of NS:", scipy.stats.mode(sample_norm).mode)
    print("[+] Median of NS:", np.median(sample_norm))
    print("[+] Minimum of NS:", np.min(sample_norm))
    print("[+] Maximum of NS:", np.max(sample_norm))
    print("[+] Standart deviation of NS:", np.std(sample_norm))
    print("[+] P-value for the null hypothesis: \
            'The sample distribution is not uniform':",
          chisquare(sample_norm).pvalue)

    sample_uniform = uniform.rvs(size=100)
    print("[+] Uniform sample:", sample_uniform)

    print("[+] Middle value of US:", np.mean(sample_uniform))
    print("[+] Mode of US:", scipy.stats.mode(sample_uniform).mode)
    print("[+] Median of US:", np.median(sample_uniform))
    print("[+] Minimum of US:", np.min(sample_uniform))
    print("[+] Maximum of US:", np.max(sample_uniform))
    print("[+] Standart deviation of US:", np.std(sample_uniform))
    print("[+] P-value for the null hypothesis: \
            'The sample distribution is not uniform':",
          chisquare(sample_uniform).pvalue)


if __name__ == "__main__":
    main()
