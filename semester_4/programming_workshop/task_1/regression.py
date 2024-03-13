import pickle

import numpy as np

from penalty import Penalty


class Regression:
    def __init__(self, iterations: int, learning_rate: float, penalty: Penalty) -> None:
        self.m: int = 0
        self.n: int = 0
        self.w: np.ndarray = np.array([])
        self.b: float = 0.0

        self.iterations = iterations
        self.learning_rate = learning_rate
        self.penalty = penalty

    def __hypothesis(
        self, weights: np.ndarray, bias: float, X: np.ndarray
    ) -> np.ndarray:
        return np.dot(X, weights) + bias

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        X = np.insert(X, 0, 1, axis=1)

        if len(y.shape) > 1:  # Проверяем, является ли массив меток классов многомерным
            print("[-] Target array should be a one dimensional array not a list")
            return

        self.m = X.shape[0]
        self.n = X.shape[1]

        self.w = np.zeros((self.n, 1))
        self.b = 0

        y = y.reshape(-1, 1)  # Преобразуем метки классов в одномерный массив

        for _ in range(1, self.iterations + 1):
            y_pred = self.__hypothesis(self.w, self.b, X)
            dw = (1 / self.m) * np.dot(X.T, (y_pred - y)) + self.penalty.derivation(
                self.w
            )
            self.w = self.w - self.learning_rate * dw

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        X_test = np.insert(X_test, 0, 1, axis=1)
        y_pred = self.__hypothesis(self.w, self.b, X_test)
        return y_pred

    def save(self, filename: str) -> None:
        with open(filename, "wb") as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)
