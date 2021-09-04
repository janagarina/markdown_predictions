import streamlit as st

import numpy as np
import pandas as pd
from markdown_predictions.trainer import get_data

file_csv = st.file_uploader("Upload a PNG image", type=([".csv"]))

if file_csv:
    # TODO: Replace with get_data function from markdown_predictions.trainer
    df = pd.read_csv(file_csv)
    df

if st.button('Set Markdowns'):
    pass