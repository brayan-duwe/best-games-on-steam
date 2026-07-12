from process_data import get_processed_data
import streamlit as st

data = get_processed_data()

st.slider('Price range')
st.table(data)
