import streamlit as st
import time


def run_simple_toast():
    st.markdown("# SimpleToast")
    st.toast('Your edited image was saved!', icon='😍')

def run_toast():
    st.markdown("# Toast")
    st.divider()
    if st.button('Three cheers'):
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hooray!', icon='🎉')

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")
def run_cook_breakfast():

    if st.button('Cook breakfast'):
        cook_breakfast()

def run_balloon_toast():
    st.markdown("# BalloonToast")
    st.divider()
    st.balloons()
    st.snow()


