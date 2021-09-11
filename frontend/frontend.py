import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from markdown_predictions.trainer import get_test_data
from csv_uploader import page_1
from markdown_selector import page_2
from exporter import page_3


# Register your pages
pages = {
    "1. CSV Uploader": page_1,
    "2. Markdown Selector": page_2,
    "3. Summary and Export": page_3,
}

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Markdown Selection Tool")

# Widget to select your page
page = st.sidebar.radio("Select your page", tuple(pages.keys()))

if "df" in st.session_state:
    num_products = len(st.session_state.df)
    st.sidebar.markdown("""
    ## Number of Products
    """)
    st.sidebar.write(str(num_products))
    
    stock = st.session_state.df["full_stock"].sum()
    st.sidebar.markdown("""
    ## Total Stock
    """)
    st.sidebar.write(str(round(stock)))
    
    target_percent = st.session_state.target/100
    unit_target = float(stock) * target_percent
    st.sidebar.markdown("""
    ## Unit Sales Target
    """)
    st.sidebar.write(str(round(unit_target)))
    
    st.sidebar.markdown("""
    ## Percentage of Target Achieved
    """)
    total_sales_pred = st.session_state.df["predicted_sales"].sum()
    pred_over_target = total_sales_pred/unit_target
    if total_sales_pred > unit_target:
        st.sidebar.progress(1.0)
    else:
        st.sidebar.progress(pred_over_target)
    st.sidebar.markdown("""
    ## Stock Per Category
    """)
    target_stock = st.session_state.df.groupby("product_category_PRE")["full_stock"].agg("sum")
    st.sidebar.write(target_stock)

# Display the selected page with the session state
pages[page]()
