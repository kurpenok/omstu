from typing import Callable

import numpy as np


def hooke_jeeves_search(target_func: Callable, initial_point: np.ndarray, eps: float):
    current_point = np.array(initial_point)
    best_point = current_point.copy()
    best_value = target_func(current_point)

    step_reduction = 0.5
    base_step = eps

    for _ in range(1000):
        # Шаг исследования
        new_point = current_point.copy()
        for i in range(len(current_point)):
            candidate_points = [new_point.copy() for _ in range(3)]
            candidate_points[i][i] += base_step
            candidate_values = [target_func(p) for p in candidate_points]
            best_candidate_idx = np.argmin(candidate_values)
            if candidate_values[best_candidate_idx] < best_value:
                new_point = candidate_points[best_candidate_idx]

        # Шаг уточнения
        if target_func(new_point) < best_value:
            current_point = new_point
            best_value = target_func(new_point)
            best_point = current_point.copy()
        else:
            base_step *= step_reduction

        # Проверка условия остановки
        if np.linalg.norm(current_point - best_point) < eps:
            break

    return best_value
