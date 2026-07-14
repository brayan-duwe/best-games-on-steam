from process_data import get_processed_data, data_filter
import streamlit as st

data = get_processed_data()
left_column, right_column = st.columns([1, 4])

def color_reviews(val):
    if val == "Positive":
        return "background-color: green"
    elif val == "Mostly positive":
        return "background-color: lightgreen"
    elif val == "Neutral":
        return "background-color: yellow"
    return "background-color: orange"

st.set_page_config(layout="wide")

with left_column:
    game_prices = st.segmented_control(
        "Price",
        ("All", "Free", "Paid")        
    )
    if game_prices != "All":
        if game_prices == "Free":
            data = data_filter(data, "Price", game_prices)
        else:
            data = data[data["Price"] != "Free"]
            
    price_range = st.slider(
        "Price range",
        100.00, 0.00,
        format="$%.2f"
        )

    if price_range < 100.00:
        if price_range > 0.00:
            data = data[data["Price_numeric"] < price_range]
        else:
            data = data[data["Price"] == "Free"]

with right_column:
    st.text_input("Search by the name: ", key="name")
    if st.session_state.name != "":
        data = data[data["Name"].str.contains(st.session_state.name, case=False, na=False)]

    styled_data = data.style.map(color_reviews, subset=["Reviews"])
    st.dataframe(styled_data, height=800, hide_index=True, column_order=("Name", "Developer", "Price", "Reviews"))