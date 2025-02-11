import pandas as pd
import streamlit as st

st.set_page_config(page_title="Data")

st.title("Information about data")

st.write(
    """
    The dataset is dedicated to monitoring car prices in Moldova.
    Using this dataset, you can solve the regression problem - 
    predict car prices depending on the brand, mileage, and so on.
    """
)

st.subheader("Example of preprocessed data")
df = pd.read_csv("../data/preprocessed_moldova_cars_dataset.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
st.dataframe(df.head())

st.subheader("Description of columns")
st.markdown(
    """
    - `make` &mdash; brand of car
    - `model` &mdash; model of car
    - `year` &mdash; year of release
    - `style` &mdash; body type
    - `distance` &mdash; mileage of car
    - `engine_capacity` &mdash; engine capacity in cm3
    - `fuel_type` &mdash; type of fuel
    - `transmission` &mdash; transmission type
    - `price` &mdash; price in euros
    """
)

st.subheader("Features of data preprocessing")
st.markdown(
    """
    - Brought the headers to lowercase and replaced the separating spaces with underscores
    - Cut out the missing values
    - Deleted duplicates
    - Recoded categorical columns (`make`, `model`, `style`, `fuel_type`, `transmission`) using LabelEncoder
    """
)
