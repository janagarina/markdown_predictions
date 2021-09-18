import sys
import joblib
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests
import altair as alt

from markdown_predictions.trainer import get_test_data


MODEL_PATH = 'markdown_model.joblib'
COLUMNS_TO_DROP = ["season_PRE"]


def save_plots(df):
    df_keys = df.reference_PRE
    for key_ref in df_keys:
        st.session_state.product_price = df[df.reference_PRE == key_ref]["price_PRE"].iloc[0]
        for md in range(0, 6):
            md /= 10
            df_tmp = df[df.reference_PRE == key_ref].copy()
            df_tmp.markdown_PRE = md
            columns_to_drop = COLUMNS_TO_DROP
            if "image_url" in df_tmp.columns:
                columns_to_drop = COLUMNS_TO_DROP + ["image_url"]
            pred = st.session_state.model.predict(df_tmp.drop(columns_to_drop, axis=1))
            if md == 0:
                plot = [(round(pred[0],0), md * 10)]
            else:
                plot.append((round(pred[0],0), md * 100))
        results = pd.DataFrame(plot, columns=["sales", "markdown"])
        results["original_price"] = st.session_state.product_price
        results["discounted_price"] = (results.original_price * ((100. - results.markdown)/100.)).apply(lambda n: round(n,2))
        base_chart = alt.Chart(results,
                 title=f"{key_ref} Unit Sales Forecast"
                ).properties(width=700, height=400).mark_line(point=True, color="#ec3361").encode(
            alt.X("markdown:O", title='Markdown %',  sort=None),
            alt.Y("sales:Q", title="Predicted 2-Week Unit Sales"),
            alt.Text("sales:Q"),
            tooltip = [alt.Tooltip("sum(sales)", title="Predicted Unit Sales"),
                   alt.Tooltip("sum(discounted_price)", title="Discount Price"),
                   alt.Tooltip("sum(original_price)", title="Original Price")]
        )
        base_chart_text = base_chart.mark_text(dy=10, dx=5, color="#ec3361").encode(text="sales:Q")
        final_chart = alt.layer(base_chart, base_chart_text)
        final_chart.save(f"{key_ref}.html")
        final_chart.save(f"{key_ref}.json")

def page_1():

    if "target" not in st.session_state:
        st.session_state.target = 0
        st.session_state.model = joblib.load(MODEL_PATH)
        st.session_state.images = {}
    
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
                for image in st.session_state.df.image_url:
                    product_ref = st.session_state.df[st.session_state.df.image_url == image]["reference_PRE"].iloc[0]
                    st.session_state.images[product_ref] = Image.open(requests.get(image, stream=True).raw)
                    
                columns_to_drop = COLUMNS_TO_DROP + ["image_url"]
            st.session_state.df["predicted_sales"] = st.session_state.model.predict(st.session_state.df.drop(columns_to_drop, axis=1))
            st.session_state.df["predicted_sales"] = st.session_state.df["predicted_sales"].astype(int)
            save_plots(st.session_state.df.drop("predicted_sales",axis=1))
        st.write(st.session_state.df)

        # Calculate and display total stock of products
        st.session_state.df["full_stock"] = st.session_state.df["avail_warehouse_stock_PRE"] + st.session_state.df["total_store_stock_PRE"]
        st.session_state.df["full_stock"] = st.session_state.df["full_stock"].astype(int)

        # Allow user to set percentage unit sales goal (session state) and display number of products needed to meet goal
        target = st.number_input("Set unit sales target (%)", min_value=0, max_value = 100, step=10, value=0, key='target')
