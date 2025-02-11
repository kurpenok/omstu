import joblib
import pandas as pd
import streamlit as st
from catboost import CatBoostRegressor
from sklearn.cluster import DBSCAN
from sklearn.ensemble import BaggingRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_absolute_percentage_error, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVR


def save_model(model, model_name: str) -> None:
    joblib.dump(model, model_name)


def load_model(model_dump_path: str):
    return joblib.load(model_dump_path)


def fit_models(X_train, y_train, X_test, y_test) -> list[float]:
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    save_model(scaler, "dumps/scaler.joblib")

    lr = LinearRegression().fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_mape = mean_absolute_percentage_error(y_test, lr_pred)
    save_model(lr, "dumps/lr.joblib")

    dbscan = DBSCAN(eps=0.5, min_samples=5).fit(X_train)
    dbscan_ss = silhouette_score(X_train, dbscan.labels_)
    save_model(dbscan, "dumps/dbscan.joblib")

    cb = CatBoostRegressor(verbose=False).fit(X_train, y_train)
    cb_pred = cb.predict(X_test)
    cb_mape = mean_absolute_percentage_error(y_test, cb_pred)
    save_model(cb, "dumps/catboost.joblib")

    br = BaggingRegressor().fit(X_train, y_train)
    br_pred = br.predict(X_test)
    br_mape = mean_absolute_percentage_error(y_test, br_pred)
    save_model(br, "dumps/bagging.joblib")

    estimators = [
        ("lr", RidgeCV()),
        ("svr", LinearSVR()),
    ]
    sr = StackingRegressor(estimators).fit(X_train, y_train)
    sr_pred = sr.predict(X_test)
    sr_mape = mean_absolute_percentage_error(y_test, sr_pred)
    save_model(sr, "dumps/stacking.joblib")

    nn = MLPRegressor().fit(X_train, y_train)
    nn_pred = nn.predict(X_test)
    nn_mape = mean_absolute_percentage_error(y_test, nn_pred)
    save_model(nn, "dumps/nn.joblib")

    return [lr_mape, dbscan_ss, cb_mape, br_mape, sr_mape, nn_mape]


def predict(data: list[list[float]]) -> list[float]:
    scaler = joblib.load("dumps/scaler.joblib")
    data = scaler.transform(data)

    lr = joblib.load("dumps/lr.joblib")
    lr_pred = lr.predict(data)

    # dbscan = joblib.load("dumps/dbscan.joblib")
    # dbscan_pred = dbscan.predict(data)

    cb = joblib.load("dumps/catboost.joblib")
    cb_pred = cb.predict(data)

    br = joblib.load("dumps/bagging.joblib")
    br_pred = br.predict(data)

    sr = joblib.load("dumps/stacking.joblib")
    sr_pred = sr.predict(data)

    nn = joblib.load("dumps/nn.joblib")
    nn_pred = nn.predict(data)

    return [lr_pred, cb_pred, br_pred, sr_pred, nn_pred]


st.set_page_config(page_title="Models")

st.title("Machine learning models")

make = st.text_input("Make:")
model = st.text_input("Model:")
year = st.text_input("Year:")
style = st.text_input("Style:")
distance = st.text_input("Distance:")
engine_capacity = st.text_input("Engine capacity (cm3):")
fuel_type = st.text_input("Fuel type:")
transmission = st.text_input("Transmission:")

if st.button("Get price"):
    data = [
        float(make),
        float(model),
        float(year),
        float(style),
        float(distance),
        float(engine_capacity),
        float(fuel_type),
        float(transmission),
    ]

    predicted_prices = predict([data])

    st.success(f"\
    [+] Predicted prices (in euro):\n\
    [+] Linear regression: {int(predicted_prices[0])}\n\
    [+] Catboost: {int(predicted_prices[1])}\n\
    [+] Bagging: {int(predicted_prices[2])}\n\
    [+] Stacking: {int(predicted_prices[3])}\n\
    [+] Neural network: {int(predicted_prices[4])}")

# df = pd.read_csv("../data/preprocessed_moldova_cars_dataset.csv")
# df.drop("Unnamed: 0", axis=1, inplace=True)
#
# y = df.loc[:, "price"]
# X = df.drop("price", axis=1)
# X_train, X_test, y_train, y_test = train_test_split(X, y)
#
# # Инициализация состояния сессии
# if "linear_regression_mape" not in st.session_state:
#     st.session_state.linear_regression_mape = 0
# if "clustering_ss" not in st.session_state:
#     st.session_state.clustering_ss = 0
# if "grad_boosting_mape" not in st.session_state:
#     st.session_state.grad_boosting_mape = 0
# if "bagging_mape" not in st.session_state:
#     st.session_state.bagging_mape = 0
# if "stacking_mape" not in st.session_state:
#     st.session_state.stacking_mape = 0
# if "nn_mape" not in st.session_state:
#     st.session_state.nn_mape = 0
#
# if st.button("Learn and save!"):
#     results = fit_models(X_train, y_train, X_test, y_test)
#
#     # Обновление значений в состоянии сессии
#     st.session_state.linear_regression_mape = results[0]
#     st.session_state.clustering_ss = results[1]
#     st.session_state.grad_boosting_mape = results[2]
#     st.session_state.bagging_mape = results[3]
#     st.session_state.stacking_mape = results[4]
#     st.session_state.nn_mape = results[5]
#
#     # Обновление текстовых меток
#     st.write(
#         f"[+] Linear regression MAPE: {st.session_state.linear_regression_mape:.4f}"
#     )
#     st.write(f"[+] Clustering silhouette score: {st.session_state.clustering_ss:.4f}")
#     st.write(f"[+] Gradient boosting MAPE: {st.session_state.grad_boosting_mape:.4f}")
#     st.write(f"[+] Bagging MAPE: {st.session_state.bagging_mape:.4f}")
#     st.write(f"[+] Stacking regression MAPE: {st.session_state.stacking_mape:.4f}")
#     st.write(f"[+] Deep neural network MAPE: {st.session_state.nn_mape:.4f}")
