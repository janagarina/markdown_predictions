import streamlit as st
import pandas as pd

number = st.number_input('Choose a markdown', min_value=0, max_value = 50, step=10, value=0)

st.write('The current number is ', number)