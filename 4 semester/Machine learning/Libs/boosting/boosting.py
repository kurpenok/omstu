import numpy as np

from sklearn.tree import DecisionTreeRegressor

class GradientBoostingRegressor:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.estimators = []

    def fit(self, X, y):
        self.mean = np.mean(y)
        y_pred = np.full_like(y, self.mean)
        for _ in range(self.n_estimators):
            gradient = y - y_pred
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, gradient)
            self.estimators.append(tree)
            update = self.learning_rate * tree.predict(X)
            y_pred += update

    def predict(self, X):
        y_pred = np.full(X.shape[0], self.mean)
        for tree in self.estimators:
            y_pred += self.learning_rate * tree.predict(X)
        return y_pred
