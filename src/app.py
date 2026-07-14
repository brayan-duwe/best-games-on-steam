from process_data import get_processed_data, data_filter
import streamlit as st

data = get_processed_data()
left_column, right_column = st.columns([1, 4])

def color_reviews(val):
    if val == "Positive":
        return "background-color: green"
    elif val == "Mostly positive":
        return "background-color: lightgreen; color: black"
    elif val == "Neutral":
        return "background-color: yellow"
    return "background-color: orange"

st.set_page_config(layout="wide")

with left_column:
    game_prices = st.segmented_control(
        "Price",
        ("All", "Free", "Paid"),
        default="All"     
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

    reviews = st.radio(
        "Reviews",
        ("All", "Positive", "Mostly positive", "Neutral", "Mostly negative")
    )
    if reviews == "All":
        pass
    elif reviews == "Positive":
        data = data[data["Reviews"] == "Positive"]
    elif reviews == "Mostly positive":
        data = data[data["Reviews"] == "Mostly positive"]
    elif reviews == "Neutral":
        data = data[data["Reviews"] == "Neutral"]
    elif reviews == "Mostly negative":
        data = data[data["Reviews"] == "Mostly negative"]

with right_column:
    st.text_input("Search by the name: ", key="name")
    if st.session_state.name != "":
        data = data[data["Name"].str.contains(st.session_state.name, case=False, na=False)]

    num_pages = len(data) // 20
    if num_pages == 0:
        num_pages = 1

    table_placeholder = st.empty()
    _, center_column, _ = st.columns([1, 2, 1])
    with center_column:
        current_page = st.pagination(num_pages)

    start = (current_page - 1) * 20
    end = start + 20
    page_data = data.iloc[start:end]
    styled_data = page_data.style.map(color_reviews, subset=["Reviews"])
    table_placeholder.dataframe(styled_data, height=738, hide_index=True, column_order=("Name", "Developer", "Price", "Reviews"))