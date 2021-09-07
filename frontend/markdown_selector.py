import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

model_path = 'markdown_model.joblib'
loaded_model = joblib.load(model_path)

def page_2():
    st.title("under construction")
    if "df" not in st.session_state:
        return True
    st.write(st.session_state.df)
    for md in range(0, 6):
        md /= 10
        df_tmp = st.session_state.df[st.session_state.df.reference_PRE == '5565201'] # one product for now
        df_tmp.markdown_PRE = md
        pred = loaded_model.predict(df_tmp.drop(["season_PRE", "full_stock"], axis=1))
        if md == 0:
            plot = [pred[0]]
            index = [md * 10]
        else:
            plot.append(pred[0])
            index.append(md * 10)

    st.write("Predicted Sales versus Markdown %")

    results = pd.DataFrame(plot, columns=["Predicted Unit Sales"])
    results.index = index
    results.index.name = "Markdown %"
    st.line_chart(results)


