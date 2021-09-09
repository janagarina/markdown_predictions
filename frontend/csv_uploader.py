import streamlit as st
import numpy as np
import pandas as pd
import sys
from markdown_predictions.trainer import get_test_data


def page_1():
    # File uploader for use to drop CSV file
    file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]))
    if file_csv:
        st.session_state.file_csv = file_csv

    if 'file_csv' in st.session_state:
        df = get_test_data(f'raw_data/{st.session_state.file_csv.name}')
        if "df" not in st.session_state:
            st.session_state.df = df
            st.session_state.df["markdown_PRE"] = 0.0
        st.write(st.session_state.df)

        st.markdown("""
        # CSV Summary
        """)

        # Calculate and display number of products in CSV
        num_products = len(st.session_state.df)
        st.write(f"Number of products: {num_products}")

        # Calculate and display total stock of products
        st.session_state.df["full_stock"] = st.session_state.df["avail_warehouse_stock_PRE"] + st.session_state.df["total_store_stock_PRE"]
        stock = st.session_state.df["full_stock"].sum()
        st.write(f"Total stock: {stock}")

        # Group total stock by sub target and category
        st.write("Stock per target & category")
        target_stock = st.session_state.df.groupby(["sub_target_PRE","product_category_PRE"])["full_stock"].agg("sum")
        st.write(target_stock)

        # Allow user to set percentage unit sales goal (session state) and display number of products needed to meet goal
        target = st.number_input("Set unit sales target (%)", min_value=0, max_value = 100, value=0)
        target_percent = target/100
        if "target_percent" not in st.session_state:
            st.session_state.target_percent = target_percent
        unit_target = float(stock) * st.session_state.target_percent
        st.write(f"Unit sales target: {round(unit_target)}")
