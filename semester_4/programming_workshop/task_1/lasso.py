import numpy as np

from penalty import l1_penalty
from regression import Regression


class LassoRegression(Regression):
    def __init__(self, l: float, iterations: int, learning_rate: float) -> None:
        self.penalty = l1_penalty(l)
        super().__init__(iterations, learning_rate, self.penalty)

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        return super().fit(X, y)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        return super().predict(X_test)
