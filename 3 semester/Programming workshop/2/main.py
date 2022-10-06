#!/usr/bin/env python3

import math

from scipy.misc import derivative


def f(x):
    return math.sin(2 * x) / math.cos(x)

def main() -> None:
    print(derivative(f, 2, dx=1e-6))


if __name__ == "__main__":
    main()
