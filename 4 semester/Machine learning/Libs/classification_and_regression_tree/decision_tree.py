import numpy as np

class DecisionTree():
    def __init__(self, max_depth=10, min_samples_split=2, min_samples_leaf=1):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.tree = {}

    def fit(self, X, y):
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        y_pred = []
        for i in range(X.shape[0]):
            y_pred.append(self._predict_sample(X[i], self.tree))
        return np.array(y_pred)

    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Рекурсивный процесс обучения
        if depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split:
            leaf_value = self._calculate_leaf_value(y)
            return {"leaf": True, "value": leaf_value}

        feature_idxs = np.random.choice(n_features, n_features, replace=False)

        best_feature_idx, best_threshold = self._find_best_split(X, y, feature_idxs)
        left_idxs, right_idxs = self._split(X[:, best_feature_idx], best_threshold)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            leaf_value = self._calculate_leaf_value(y)
            return {"leaf": True, "value": leaf_value}

        left_subtree = self._build_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right_subtree = self._build_tree(X[right_idxs, :], y[right_idxs], depth+1)

        return {"leaf": False,
                "feature_idx": best_feature_idx,
                "threshold": best_threshold,
                "left_subtree": left_subtree,
                "right_subtree": right_subtree}

    def _find_best_split(self, X, y, feature_idxs):
        best_gain = -1
        split_idx, split_threshold = None, None
        for feature_idx in feature_idxs:
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                left_idxs, right_idxs = self._split(X[:, feature_idx], threshold)
                if len(left_idxs) == 0 or len(right_idxs) == 0:
                    continue
                gain = self._calculate_gain(y, left_idxs, right_idxs)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feature_idx
                    split_threshold = threshold
        return split_idx, split_threshold

    def _calculate_gain(self, y, left_idxs, right_idxs):
        p = len(left_idxs) / len(y)
        left_gini = self._calculate_gini(y[left_idxs])
        right_gini = self._calculate_gini(y[right_idxs])
        gain = self._calculate_gini(y) - p * left_gini - (1 - p) * right_gini
        return gain

    def _calculate_gini(self, y):
        n_samples = len(y)
        if n_samples == 0:
            return 0
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / np.sum(counts)
        gini = 1 - np.sum(np.square(probabilities))
        return gini

    def _split(self, feature, threshold):
        left_idxs = np.where(feature <= threshold)[0]
        right_idxs = np.where(feature > threshold)[0]
        return left_idxs, right_idxs

    def _calculate_leaf_value(self, y):
        leaf_value = np.mean(y)
        return leaf_value

    def _predict_sample(self, sample, tree):
        if tree["leaf"]:
            return tree["value"]
        feature_value = sample[tree["feature_idx"]]
        if feature_value <= tree["threshold"]:
            return self._predict_sample(sample, tree["left_subtree"])
        else:
            return self._predict_sample(sample, tree["right_subtree"])
