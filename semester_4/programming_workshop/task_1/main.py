import numpy as np
from sklearn.datasets import make_regression
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split

from elastic_net import ElasticNetRegression
from lasso import LassoRegression


def main() -> None:
    X, y = make_regression(n_samples=50_000, n_features=2)
    y = y[:, np.newaxis]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    params = {
        "iterations": 100,
        "learning_rate": 0.01,
        "l": 0.0001,
    }
    lasso_model = LassoRegression(**params)
    lasso_model.fit(np.array(X_train), np.array(y_train))
    y_pred = lasso_model.predict(np.array(X_test))
    print(f"[+] R2-score: {r2_score(y_test, y_pred)}")
    print(f"[+] MAPE: {mean_absolute_percentage_error(y_test, y_pred)}")

    params = {
        "iterations": 100,
        "learning_rate": 0.01,
        "l": 0.0001,
        "l_ratio": 0.1,
    }
    elastic_net_model = ElasticNetRegression(**params)
    elastic_net_model.fit(np.array(X_train), np.array(y_train))
    y_pred = elastic_net_model.predict(np.array(X_test))
    print(f"[+] R2-score: {r2_score(y_test, y_pred)}")
    print(f"[+] MAPE: {mean_absolute_percentage_error(y_test, y_pred)}")


if __name__ == "__main__":
    main()
