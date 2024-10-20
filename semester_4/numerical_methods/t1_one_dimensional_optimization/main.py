import math

from dichotomy import dichotomy_search
from fibonacci import fibonacci_search
from golden_ratio import golden_ratio_search


def f(x: float) -> float:
    return x**4 / math.log(x)


def main() -> None:
    a = 1.1
    b = 1.5
    eps = 0.0001

    print(f"[+] Dichotomy: {dichotomy_search(f, a, b, eps):.{2}f}")
    print(f"[+] Fibonacci: {fibonacci_search(f, a, b, eps):.{2}f}")
    print(f"[+] Golden ratio: {golden_ratio_search(f, a, b, eps):.{2}f}")


if __name__ == "__main__":
    main()
