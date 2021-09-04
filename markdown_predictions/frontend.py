import streamlit as st

import numpy as np
import pandas as pd
from markdown_predictions.trainer import get_data

file_csv = st.file_uploader("Upload a PNG image", type=([".csv"]))
