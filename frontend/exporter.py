import streamlit as st
import numpy as np
import pandas as pd

def page_3():
    export_df = st.session_state.df[['reference_PRE','markdown_PRE']]
    st.write(export_df)
    if st.button('Download CSV'):
        export_df.to_csv('../markdown_export.csv')