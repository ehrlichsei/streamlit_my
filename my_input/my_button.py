import streamlit as st

def run_button():
    st.markdown("# Button")
    st.divider()
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")
