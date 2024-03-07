import math

from gauss_seidel import gauss_seidel_search


def f(x: list[float]) -> float:
    A = 20
    a = 3
    b = 2
    return A - ((x[0] - a) * math.exp(-x[0] + a)) - ((x[1] - b) * math.exp(-x[1] + b))


def main() -> None:
    n = 2
    eps = 0.0001

    print(f"[+] Gauss-Seidel: {gauss_seidel_search(f, n, eps)}")


if __name__ == "__main__":
    main()
