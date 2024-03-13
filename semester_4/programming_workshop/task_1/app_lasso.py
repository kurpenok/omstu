import numpy as np
import streamlit as st
from sklearn.datasets import make_regression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

from lasso import LassoRegression


def main():
    st.title("Lasso regressions demo")

    st.sidebar.header("Settings")
    l_value = st.sidebar.number_input(
        "Penalty Value (l)", min_value=0.0, max_value=10.0, step=0.01, value=1.0
    )
    iterations = st.sidebar.number_input(
        "Iterations", min_value=100, max_value=5000, step=100, value=1000
    )
    learning_rate = st.sidebar.number_input(
        "Learning Rate", min_value=0.001, max_value=0.1, step=0.001, value=0.01
    )

    st.sidebar.subheader("Model Performance")
    mape_display = st.empty()

    X, y = make_regression(n_samples=50_000, n_features=2)
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    iterations = 10000
    learning_rate = 0.01
    if st.sidebar.button("Train Model"):
        lasso_model = LassoRegression(
            l=l_value, iterations=iterations, learning_rate=learning_rate
        )
        lasso_model.fit(np.array(X_train), np.array(y_train))
        y_pred = lasso_model.predict(np.array(X_test))
        mape = mean_absolute_percentage_error(y_test, np.round(y_pred))
        mape_display.success(f"MAPE: {mape}")

    st.subheader("Dataset Preview")
    st.write("X shape:", X.shape)
    st.write("y shape:", y.shape)
    st.write("Sample X:", X[0])
    st.write("Sample y:", y[0])

    st.subheader("Model Parameters")
    st.write("Penalty Value (l):", l_value)
    st.write("Iterations:", iterations)
    st.write("Learning Rate:", learning_rate)


if __name__ == "__main__":
    main()
