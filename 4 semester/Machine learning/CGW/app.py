import pickle

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error

import streamlit as st


def main():
    model = load_model("model/model.pkl")
    test_data = load_test_data("data/updated_df.csv")
    y_test = test_data["Appliances"]
    test_data = test_data.drop(labels=["Appliances"], axis=1)
    
    page = st.sidebar.selectbox(
        "Выберите страницу",
        ["Описание задачи и данных", "Запрос к модели"]
    )

    if page == "Описание задачи и данных":
        st.title("Описание задачи и данных")
        st.write("Выберите страницу слева")

        st.header("Описание задачи")
        st.markdown("""Розничная компания «ABC Private Limited» хочет понять покупательское поведение (в частности, сумму покупки) по отношению к различным продуктам разных категорий. Они поделились сводкой покупок различных клиентов для избранных продуктов большого объема за последний месяц.
Набор данных также содержит демографические данные клиентов, сведения о продукте и общую сумму покупки за последний месяц. 
Теперь они хотят построить модель для прогнозирования количества покупок клиентов по различным продуктам, которая поможет им создавать персонализированные предложения для клиентов по разным продуктам.""")

        st.header("Описание данных")
        st.markdown("""Предоставленные данные:
* Appliances – ,
* lights – ,
* T1 – ,
* RH_1 – ,
* T2 – ,
* RH_2 – ,
* T3 – ,
* RH_3 – ,
* T3 – ,
* RH_3 – ,
* T4 – ,
* RH_4 – ,
* T5 – ,
* RH_5 – ,
* T6 – ,
* RH_7 – ,
* T8 – ,
* RH_8 – ,
* T9 – ,
* RH_9 – ,
* T_out – ,
* Press_mm_hg - ,
* RH_out - ,
* Windspeed - ,
* Visibility - ,
* Tdewpoint - ,

К категориальным признакам относятся:
* Дата

К численным признакам относятся все остальные столбцы.""")

    elif page == "Запрос к модели":
        st.title("Запрос к модели")
        st.write("Выберите страницу слева")
        request = st.selectbox(
            "Выберите запрос",
            ["RMSE", "Первые 5 предсказанных значений", "Пользовательский пример"],
        )

        if request == "RMSE":
            st.header("Корень из среднеквадратичной ошибки")
            y_pred = model.predict(test_data)
            rmse = mean_squared_error(y_test, y_pred)
            st.write(f"{rmse}")

        elif request == "Первые 5 предсказанных значений":
            st.header("Первые 5 предсказанных значений")
            y_pred = model.predict(test_data.iloc[:5, :])
            for pred in y_pred:
                st.write(f"{pred:.2f}")

        elif request == "Пользовательский пример":
            st.header("Пользовательский пример")

            lights = st.number_input("Lights")
            t1 = st.number_input("T1")
            rh_1 = st.number_input("RH_1")
            t2 = st.number_input("T2")
            rh_2 = st.number_input("RH_2")
            t3 = st.number_input("T3")
            rh_3 = st.number_input("RH_3")
            t4 = st.number_input("T4")
            rh_4 = st.number_input("RH_4")
            t5 = st.number_input("T5")
            rh_5 = st.number_input("RH_5")
            t6 = st.number_input("T6")
            rh_6 = st.number_input("RH_6")
            t7 = st.number_input("T7")
            rh_7 = st.number_input("RH_7")
            t8 = st.number_input("T8")
            rh_8 = st.number_input("RH_8")
            t9 = st.number_input("T9")
            rh_9 = st.number_input("RH_9")
            t_out = st.number_input("T_out")
            press_mm_hg = st.number_input("Press_mm_hg")
            rh_out = st.number_input("RH_out")
            windspeed = st.number_input("Windspeed")
            visibility = st.number_input("Visibility")
            tdewpoint = st.number_input("Tdewpoint")

            if st.button("Предсказать"):
                data = [lights, t1, rh_1, t2, rh_2, t3, rh_3, t4, rh_4, t5, rh_5, t6, rh_6, t7, rh_7, t8, rh_8, t9, rh_9, t_out, press_mm_hg, rh_out, windspeed, visibility, tdewpoint]
                data = np.array(data).reshape((1, -1))
                pred = model.predict(data)
                st.write(f"Предсказанное значение: {pred[0]:.2f}")
            else:
                pass


@st.cache_data
def load_model(path_to_file):
    with open(path_to_file, "rb") as model_file:
        model = pickle.load(model_file)
    return model


@st.cache_data
def load_test_data(path_to_file):
    df = pd.read_csv(path_to_file, index_col="Unnamed: 0")
    return df


if __name__ == "__main__":
    main()
