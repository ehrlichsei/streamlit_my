import time
import streamlit as st

def run_status_container():
    st.markdown("# status_container")
    st.divider()
    st.status("Downloading data...")
    time.sleep(2)
    st.status("Found URL.")
    time.sleep(1)
    st.status("Downloading data...")
    time.sleep(1)

    st.button("Rerun")