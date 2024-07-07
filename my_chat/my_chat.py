import streamlit as st

def run_chat():
    st.markdown("# Chat")
    st.divider()
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")