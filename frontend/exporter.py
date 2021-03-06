import streamlit as st
import numpy as np
import pandas as pd


TABLE_NAMES = {
               "reference_PRE": "Product ID",
               "markdown_PRE": "Markdown",
               "predicted_sales": "Predicted Sales (Units)"
               }

def page_3():
    st.title("Predicted 2-week Sales Summary")
    # Show dataframe with selected markdowns and predicted sales
    
    if not "df" in st.session_state:
        return True

    export_df = st.session_state.df[["reference_PRE","markdown_PRE","predicted_sales"]].rename(columns=TABLE_NAMES)
    st.write(export_df)
    
    # Calculate and display the sales target
    target_sales = ((st.session_state.target/100) * st.session_state.df["full_stock"]).sum()
    st.write(f"Sales target: {'{:,}'.format(round(target_sales))}")
    
    # Calculate and display sum predicted sales
    total_sales_pred = export_df["Predicted Sales (Units)"].sum()
    st.write(f"Predicted 2-week sales: {'{:,}'.format(round(total_sales_pred))}")
    
    # Calculate and display the precentage of achieved sales
    pred_over_target = (total_sales_pred/round(target_sales))
    percent_to_target = round((pred_over_target * 100),2)
    st.write(f"Percentage achieved: {percent_to_target}%")
    
    # Save CSV of export_df
    st.download_button(
        label = "Download CSV",
        data = export_df.to_csv(index=False).encode(),
        file_name = "markdown_export.csv",
        mime = "text/csv"
    )
