import streamlit as st

st.image(
    "https://blogs.lawrence.edu/careercenter/files/2021/03/nfTYe3Ec_400x400.jpg",
    width=200)
st.write("To start using this engine, please enter your email below and use the side bar to navigate to search or dictionary. ")
recipient_email = st.text_input("Please enter your email: ")
