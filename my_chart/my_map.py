import streamlit as st
import pandas as pd
import numpy as np

def run_map():
    st.markdown("# Map")
    st.divider()
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [48.13, 11.58],
        columns=['lat', 'lon'])

    st.map(df)