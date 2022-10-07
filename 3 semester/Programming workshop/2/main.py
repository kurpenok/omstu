#!/usr/bin/env python3

import math

from scipy.misc import derivative
from scipy.integrate import quad
from sympy import symbols, diff, integrate, sin, cos


def f(x):
    return math.sin(2 * x) / math.cos(x)


def integrand(x):
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

    print("[+] Optimal value:", )
    print("[+] Optimal solution:", )


if __name__ == "__main__":
    main()
