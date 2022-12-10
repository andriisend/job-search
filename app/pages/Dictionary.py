import requests
import json 
import streamlit as st
from models import dictionary_criteria, get_label_from_criteria
from api import fetch_code_list

st.markdown("# Code Dictionary")

user_input = st.selectbox(
    'Please choose a search criteria',
    dictionary_criteria, format_func=get_label_from_criteria)

if user_input != None:
  search_input = st.text_input(user_input.help_text)
  if st.button("Search"):
    user_input.search(search_input, fetch_code_list(user_input), st)
