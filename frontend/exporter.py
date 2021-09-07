import streamlit as st
import numpy as np
import pandas as pd

def page_3():
    export_df = st.session_state.df[["reference_PRE","markdown_PRE"]]
    # TODO: update with output after model/markdown selector page updates
    export_df["predicted_sales"] = [700,100,200,320,600,239,543,10,578]
    total_sales_pred = export_df["predicted_sales"].sum()
    st.write(export_df)
    target_sales = (st.session_state.target_percent * st.session_state.df["full_stock"]).sum()
    st.write(f"Sales target: {round(target_sales)}")
    st.write(f"Predicted sales {total_sales_pred}")
    pred_over_target = (total_sales_pred/round(target_sales))
    percent_to_target = round((pred_over_target * 100),2)
    st.write(f"Percentage achieved: {percent_to_target}%")
    if st.button("Download CSV"):
        export_df.to_csv("../markdown_export.csv")