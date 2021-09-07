import streamlit as st
import numpy as np
import pandas as pd
from markdown_predictions.trainer import get_test_data


def page_1():
    file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]))

    if file_csv:
        df = get_test_data(f"../raw_data/{file_csv.name}")
        if "df" not in st.session_state:
            st.session_state.df = df
            st.session_state.df["markdown_PRE"] = 0.0
    st.write(st.session_state.df)
    st.write("CSV Summary")
    num_products = len(st.session_state.df)
    st.write(f"Number of products: {num_products}")
    st.session_state.df["full_stock"] = st.session_state.df["avail_warehouse_stock_PRE"] + st.session_state.df["total_store_stock_PRE"]
    stock = st.session_state.df["full_stock"].sum()
    st.write(f"Total stock: {stock}")
    st.write("Stock per target & category")
    # # TODO: Updte column names after get_data merge
    # target_stock = df.groupby(["Sous-cible","Catégorie"])["full_stock"].agg("sum")
    # target_stock
    target = st.number_input("Set unit sales target (%)", min_value=0, max_value = 100, value=0)
    target_percent = target/100
    if "target_percent" not in st.session_state:
        st.session_state.target_percent = target_percent
    unit_target = float(stock) * target_percent
    st.write(f"Unit sales target: {round(unit_target)}")