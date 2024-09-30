import numpy as np
from collections import Counter


def accuracy(actual, predicted):
    total = len(actual)
    correct = 0

    for i in range(total):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / total


def precision(true_positives, true_negatives, false_positives):
    return true_positives / (true_positives + false_positives)


def recall(true_positives, true_negatives, false_negatives):
    return true_positives / (true_positives + false_negatives)


def f1(precision, recall):
    if precision + recall == 0:
        return 0
    else:
        return 2 * precision * recall / (precision + recall)


# Функция для вычисления евклидова расстояния между двумя точками
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[: self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_nearest_labels).most_common(1)[0][0]
