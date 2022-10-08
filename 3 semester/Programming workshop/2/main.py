#!/usr/bin/env python3

import math

import numpy as np

from scipy.misc import derivative
from scipy.integrate import quad
from scipy.optimize import Bounds, LinearConstraint, minimize

from sympy import symbols, diff, integrate, sin, cos


def f(x) -> float:
    return math.sin(2 * x) / math.cos(x)


def g(x) -> float:
    return (x[0] - 3)**2 + (x[1] - 8)**2


def integrand(x) -> None:
    return sin(2 * x) / cos(x)


def main() -> None:
    x0 = 2
    a = 2
    b = 3

    print("[+] Equation: y = sin(2x) / cos(x)")
    print("[+] First derivative mean:", derivative(f, x0, dx=1e-6))
    print("[+] Second derivative mean:", derivative(f, x0, dx=1e-6, n=2))

    x = symbols("x")
    print("[+] Symbolic representation of the first derivative:", diff(sin(2 * x) / cos(x)))
    print("[+] Symbolic representation of the second derivative:", diff(diff(sin(2 * x) / cos(x))))

    print("[+] Definite integral:", quad(integrand, a, b))

    print("[+] Undefined integral:", integrate(sin(2 * x) / cos(x), x))

    x0 = np.array([1, 1])
    bounds = Bounds(lb=0, ub=np.inf)
    lc = LinearConstraint([[-2, 1], [3, 4]], lb=[2, -6], ub=[2, -6])
    print("[+] Optimazed values:", minimize(
        fun=g,
        x0=x0,
        method="trust-constr",
        bounds=bounds,
        constraints=lc,
        tol=1e-3
        ).x)


if __name__ == "__main__":
    main()
