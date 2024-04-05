import numpy as np

from lagrange_multipliers import langrange_multipliers_search


def phi(x: np.ndarray) -> float:
    return pow(x[0], 2) + 1.5 * x[1] - 2


def f(x: np.ndarray) -> float:
    return x[0] - x[1]


def main() -> None:
    langrange_multipliers_search()


if __name__ == "__main__":
    main()
