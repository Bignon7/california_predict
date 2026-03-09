import streamlit as st


def show_default_page():
    st.title("Default Page")
    st.image("404_img.png", caption="La page demandée n'existe pas", width=400, )
