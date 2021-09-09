import sys
import joblib
import streamlit as st
import numpy as np
import pandas as pd

from markdown_predictions.trainer import get_test_data


MODEL_PATH = 'markdown_model.joblib'


def page_1():

    if "target" not in st.session_state:
        st.session_state.target = 0
        st.session_state.model = joblib.load(MODEL_PATH)
    
    # File uploader for use to drop CSV file
    file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]))
    if file_csv:
        st.session_state.file_csv = file_csv


    if 'file_csv' in st.session_state:
        df = get_test_data(f'raw_data/{st.session_state.file_csv.name}')
        if "df" not in st.session_state:
            st.session_state.df = df
            st.session_state.df["markdown_PRE"] = 0.0
            st.session_state.df["predicted_sales"] = st.session_state.model.predict(st.session_state.df.drop(["season_PRE"], axis=1))
            st.session_state.df["predicted_sales"] = st.session_state.df["predicted_sales"].astype(int)
        st.write(st.session_state.df)

        st.markdown("""
        # CSV Summary
        """)

        # Calculate and display number of products in CSV
        num_products = len(st.session_state.df)
        st.write(f"Number of products: {num_products}")

        # Calculate and display total stock of products
        st.session_state.df["full_stock"] = st.session_state.df["avail_warehouse_stock_PRE"] + st.session_state.df["total_store_stock_PRE"]
        st.session_state.df["full_stock"] = st.session_state.df["full_stock"].astype(int)
        stock = st.session_state.df["full_stock"].sum()
        st.write(f"Total stock: {stock}")

        # Group total stock by sub target and category
        st.write("Stock per target & category")
        target_stock = pd.DataFrame(st.session_state.df.groupby(["sub_target_PRE","product_category_PRE"])["full_stock", "predicted_sales"].agg("sum"))
        target_stock["full_stock"] = target_stock["full_stock"].apply(lambda x: "{:,}".format(x).replace(".0", ""))
        target_stock["predicted_sales"] = target_stock["predicted_sales"].apply(lambda x: "{:,}".format(round(x)).replace(".0", ""))
        st.write(target_stock.rename(columns={"full_stock": "Total Stock", "predicted_sales": "Predicted Sales (Units)"}))

        # Allow user to set percentage unit sales goal (session state) and display number of products needed to meet goal
        target = st.number_input("Set unit sales target (%)", min_value=0, max_value = 100, value=0, key='target')

        target_percent = st.session_state.target/100
        unit_target = float(stock) * target_percent
        st.write(f"Unit sales target: {round(unit_target)}")

        
        
