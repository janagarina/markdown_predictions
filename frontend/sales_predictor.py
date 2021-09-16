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
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    <style>
    stSidebar.stProgress .st-bo {
        background-color: green;
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
    st.sidebar.markdown(f"""
    ## Number of Products
    # {round(num_products)}
    """)
    
    stock = st.session_state.df["full_stock"].sum()
    st.sidebar.markdown(f"""
    ## Total Stock
    # {'{:,}'.format(round(stock))}
    """)
    
    target_percent = st.session_state.target/100
    unit_target = float(stock) * target_percent
    st.sidebar.markdown(f"""
    ## Unit Sales Target
    # {'{:,}'.format(round(unit_target))}
    """)
    
    total_sales_pred = st.session_state.df["predicted_sales"].sum()
    pred_over_target = total_sales_pred/unit_target
    st.sidebar.markdown(f"""
    ## Percentage of Target Achieved
    # {round((pred_over_target * 100),2)}%
    """)
    progress = st.sidebar.progress(0)
    if total_sales_pred > unit_target:
        progress.progress(1.0,)
    else:
        progress.progress(pred_over_target)
    st.sidebar.markdown("""
    ## Stock Per Product Family
    """)
    target_stock = pd.DataFrame(st.session_state.df.groupby("family_PRE")["full_stock"].agg("sum"))
    target_stock["full_stock"] = target_stock["full_stock"].apply(lambda x: "{:,}".format(x).replace(".0", ""))
    st.sidebar.write(target_stock.rename(columns={"full_stock": "Total Stock"}))
    
    # if "product_idx" in st.session_state:
    #     key_ref = st.session_state.df.reference_PRE.iloc[st.session_state.product_idx]
    #     st.sidebar.image(st.session_state.df.image_url[st.session_state.df.reference_PRE == key_ref].iloc[0], use_column_width='auto')

# Display the selected page with the session state
pages[page]()
