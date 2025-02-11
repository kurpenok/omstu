import numpy as np
import streamlit as st
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from elastic_net import ElasticNetRegression


def main():
    st.title("Elastic-Net regressions demo")

    st.sidebar.header("Settings")
    l = st.sidebar.slider(
        "L1/L2 Ratio (l_ratio)", min_value=0.0, max_value=1.0, step=0.01, value=0.5
    )
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
    accuracy = st.empty()

    X, y = make_classification(
        n_samples=1000, n_features=20, n_classes=2, random_state=42
    )
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    iterations = 10000
    learning_rate = 0.01
    if st.sidebar.button("Train Model"):
        elastic_net_model = ElasticNetRegression(
            l=l_value, l_ratio=l, iterations=iterations, learning_rate=learning_rate
        )
        elastic_net_model.fit(np.array(X_train), np.array(y_train))
        y_pred = elastic_net_model.predict(np.array(X_test))
        acc = accuracy_score(y_test, np.round(y_pred))
        accuracy.success(f"Accuracy: {acc}")

    st.subheader("Dataset Preview")
    st.write("X shape:", X.shape)
    st.write("y shape:", y.shape)
    st.write("Sample X:", X[0])
    st.write("Sample y:", y[0])

    st.subheader("Model Parameters")
    st.write("L1/L2 Ratio (l_ratio):", l)
    st.write("Penalty Value (l):", l_value)
    st.write("Iterations:", iterations)
    st.write("Learning Rate:", learning_rate)


if __name__ == "__main__":
    main()
