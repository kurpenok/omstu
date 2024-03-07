from typing import Callable


def optimize(f: Callable, axes: list[float], i: int, eps: float) -> float:
    axes_left = axes[:]
    axes_right = axes[:]

    axes_left[i] -= eps
    axes_right[i] += eps

    while not (f(axes_left) > f(axes) < f(axes_right)):
        if f(axes_left) < f(axes) < f(axes_right):
            axes_right, axes = axes[:], axes_left[:]
            axes_left[i] -= eps
        elif f(axes_left) > f(axes) > f(axes_right):
            axes_left, axes = axes[:], axes_right[:]
            axes_right[i] += eps

    return axes[i]


def gauss_seidel_search(f: Callable, n: int, eps: float) -> float:
    axes = [0.0] * n

    for i in range(n):
        axes[i] = optimize(f, axes, i, eps)

    return f(axes)
