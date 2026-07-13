from process_data import get_processed_data, data_filter
import streamlit as st

data = get_processed_data()

# st.slider('Price range')
# st.table(data)

game_prices = st.selectbox(
    "Price",
    ("All", "Free", "Paid")        
)

if game_prices != "All":
    if game_prices == "Free":
        data = data_filter(data, "Price", game_prices)
    else:
        data = data[data["Price"] != "Free"]

st.text_input("Search by the name: ", key="name")
if st.session_state.name != "":
    data = data[data["Name"].str.contains(st.session_state.name, case=False, na=False)]

st.dataframe(data.style.highlight_max(axis=0))
