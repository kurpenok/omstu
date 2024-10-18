from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Data visualization")

st.title("Data visualization")

df = pd.read_csv("../data/preprocessed_moldova_cars_dataset.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

fig, axs = plt.subplots(2, 2, figsize=(20, 16))

unique_makes = list(df["make"].unique())
counts = df["make"].value_counts() / len(df)
axs[0, 0].bar(unique_makes, counts)
axs[0, 0].set_title("Distribution of car brands")
axs[0, 0].set_xlabel("Car brand")
axs[0, 0].set_ylabel("Fraction")

sns.heatmap(df.corr(), ax=axs[0, 1])
axs[0, 1].set_title("Correlations heatmap")

prices_distributions = Counter(df["price"].values)
axs[1, 0].bar(list(prices_distributions.keys()), list(prices_distributions.values()))
axs[1, 0].set_title("Distribution of car prices")
axs[1, 0].set_xlabel("Price")
axs[1, 0].set_ylabel("Count")

st.pyplot(fig)
