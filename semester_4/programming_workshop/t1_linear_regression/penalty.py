import abc

import numpy as np


class Penalty:
    def __init__(self, l: float = 1, l_ratio: float = 1) -> None:
        self.l = l
        self.l_ratio = l_ratio

    def __call__(self, weights: np.ndarray) -> np.ndarray:
        return self.l * np.sum(np.square(weights))

    @abc.abstractmethod
    def derivation(self, weights: np.ndarray):
        raise NotImplementedError()


class l1_penalty(Penalty):
    def __init__(self, l: float) -> None:
        super().__init__(l)

    def __call__(self, weights: np.ndarray) -> np.ndarray:
        return super().__call__(weights)

    def derivation(self, weights: np.ndarray) -> np.ndarray:
        return self.l * np.sign(weights)


class l2_penalty(Penalty):
    def __init__(self, l: float) -> None:
        super().__init__(l)

    def __call__(self, weights: np.ndarray) -> np.ndarray:
        return super().__call__(weights)

    def derivation(self, weights: np.ndarray) -> np.ndarray:
        return self.l * 2 * weights


class l1_l2_penalty(Penalty):
    def __init__(self, l: float = 1, l_ratio: float = 1) -> None:
        super().__init__(l, l_ratio)

    def __call__(self, weights: np.ndarray) -> np.ndarray:
        l1_contribution = self.l_ratio * self.l * np.sum(np.abs(weights))
        l2_contribution = (1 - self.l_ratio) * self.l * 0.5 * np.sum(np.square(weights))
        return l1_contribution + l2_contribution

    def derivation(self, weights: np.ndarray):
        l1_derivation = self.l * self.l_ratio * np.sign(weights)
        l2_derivation = self.l * (1 - self.l_ratio) * weights
        return l1_derivation + l2_derivation
