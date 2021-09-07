import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from markdown_predictions.trainer import get_test_data
from csv_uploader import page_1
from markdown_selector import page_2
from exporter import page_3


# Register your pages
pages = {
    "1. CSV Uploader": page_1,
    "2. Markdown Selector": page_2,
    "3. Summary and Export": page_3,
}

st.sidebar.title("Markdown Selection Tool")

# Widget to select your page
page = st.sidebar.radio("Select your page", tuple(pages.keys()))

# Display the selected page with the session state
pages[page]()
