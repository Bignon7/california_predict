import streamlit as st
from prediction_page import show_prediction_page
from stats_page import show_stats_page
from default_page import show_default_page


st.set_page_config(page_title="Californian houses price prediction", page_icon=":house:")

page = st.sidebar.selectbox("Select a page", ["Prediction", "Statistics", "Default"])

if page == "Prediction":
    show_prediction_page()
elif page == "Statistics":
    show_stats_page()
else:
    show_default_page()

