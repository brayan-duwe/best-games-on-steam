from process_data import get_processed_data, data_filter
import streamlit as st

data = get_processed_data()
st.set_page_config(layout="wide")

left_column, right_column = st.columns([1, 4])

with left_column:
    game_prices = st.selectbox(
        "Price",
        ("All", "Free", "Paid")        
    )
    if game_prices != "All":
        if game_prices == "Free":
            data = data_filter(data, "Price", game_prices)
        else:
            data = data[data["Price"] != "Free"]
            
    price_range = st.slider(
        "Price range $",
        0.00, 100.00
        )

    if price_range > 0.00:
        data = data[data["Price_numeric"] < price_range]



with right_column:
    st.text_input("Search by the name: ", key="name")
    if st.session_state.name != "":
        data = data[data["Name"].str.contains(st.session_state.name, case=False, na=False)]

    st.dataframe(data, height=800, hide_index=True, column_order=("Name", "Developer", "Price", "Reviews"))