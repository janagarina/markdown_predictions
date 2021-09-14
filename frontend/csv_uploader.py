import sys
import joblib
import streamlit as st
import numpy as np
import pandas as pd

from markdown_predictions.trainer import get_test_data


MODEL_PATH = 'markdown_model.joblib'
COLUMNS_TO_DROP = ["season_PRE"]


def page_1():

    if "target" not in st.session_state:
        st.session_state.target = 0
        st.session_state.model = joblib.load(MODEL_PATH)
    
    # File uploader for use to drop CSV file
    file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]), key='file_csv')
    if st.session_state.file_csv:
        new_df=pd.read_csv(st.session_state.file_csv)
        new_df.to_csv(st.session_state.file_csv.name)
 

    if 'file_csv' in st.session_state and file_csv is not None:
        df=get_test_data(st.session_state.file_csv.name)
        if "df" not in st.session_state:
            st.session_state.df = df
            st.session_state.df["markdown_PRE"] = 0.0
            columns_to_drop = COLUMNS_TO_DROP
            if "image_url" in st.session_state.df.columns:
                columns_to_drop = COLUMNS_TO_DROP + ["image_url"]
            st.session_state.df["predicted_sales"] = st.session_state.model.predict(st.session_state.df.drop(columns_to_drop, axis=1))
            st.session_state.df["predicted_sales"] = st.session_state.df["predicted_sales"].astype(int)
        st.write(st.session_state.df)

        # Calculate and display total stock of products
        st.session_state.df["full_stock"] = st.session_state.df["avail_warehouse_stock_PRE"] + st.session_state.df["total_store_stock_PRE"]
        st.session_state.df["full_stock"] = st.session_state.df["full_stock"].astype(int)

        # Allow user to set percentage unit sales goal (session state) and display number of products needed to meet goal
        target = st.number_input("Set unit sales target (%)", min_value=0, max_value = 100, step=10, value=0, key='target')
