import streamlit as st
import numpy as np
import pandas as pd

def page_3():
    st.title("Predicted Sales Summary")
    # Show dataframe with selected markdowns and predicted sales
    export_df = st.session_state.df[["reference_PRE","markdown_PRE","predicted_sales"]]
    st.write(export_df)
    
    # Calculate and display the sales target
    target_sales = ((st.session_state.target/100) * st.session_state.df["full_stock"]).sum()
    st.write(f"Sales target: {round(target_sales)}")
    
    # Calculate and display sum predicted sales
    total_sales_pred = export_df["predicted_sales"].sum()
    st.write(f"Predicted sales {round(total_sales_pred)}")
    
    # Calculate and display the precentage of achieved sales
    pred_over_target = (total_sales_pred/round(target_sales))
    percent_to_target = round((pred_over_target * 100),2)
    st.write(f"Percentage achieved: {percent_to_target}%")
    
    # Save CSV of export_df
    if st.button("Download CSV"):
        export_df.to_csv("markdown_export.csv")
