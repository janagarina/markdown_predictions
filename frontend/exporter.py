import streamlit as st
import numpy as np
import pandas as pd

def page_3():
    d={'col1':['1','2','3'],'col2':[.3,.4,.1],'col3':[250,300,145]}
    export_df = pd.DataFrame(data=d)
    st.write(export_df)
    st.write(st.session_state.df)