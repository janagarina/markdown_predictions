import streamlit as st
import numpy as np
import pandas as pd
from markdown_predictions.trainer import get_data

'''
# Markdown Selection Tool
'''

file_csv = st.file_uploader("Upload your CSV here", type=([".csv"]))

if file_csv:
    # TODO: Replace with get_data function from markdown_predictions.trainer
    df = pd.read_csv(file_csv)
    df
    # TODO: Fill out remainng summary items once get_data is implemented
    st.write('CSV Summary')
    num_products = len(df)
    st.write(f'Number of products: {num_products}')
    df['full_stock'] = df['warehouse'] + df['store_stock']
    stock = df['full_stock'].sum()
    st.write(f'Total stock: {stock}')
    st.write('Stock per target & category')
    # TODO: Updte column names after get_data merge
    target_stock = df.groupby(['Sous-cible','Catégorie'])['full_stock'].agg('sum')
    target_stock
    target = st.number_input('Set unit sales target', min_value=0, max_value = 100, value=0)
    target_percent = target/100
    unit_target = float(stock) * target_percent
    st.write(f'Unit sales target: {round(unit_target)}')
    

if st.button('Set Markdowns'):
    pass

number = st.number_input('Choose a markdown', min_value=0, max_value = 50, step=10, value=0)
st.write('The current number is ', number)
