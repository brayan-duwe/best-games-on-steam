import json
import pandas as pd

COL_NAME = "name"
COL_PRICE = "price"
COL_POSITIVE = "positive"
COL_NEGATIVE = "negative"
COL_DEVELOPER = "developer"
COL_REVIEWS = "reviews"

def sheet_data(): 
    with open("data/raw_data.json", "r") as content:
        data = json.load(content)
    result = pd.json_normalize(list(data.values()))

    return result

def dollar_converter(data):
    data["Price_numeric"] = (pd.to_numeric(data[COL_PRICE]) / 100).round(2)
    data[COL_PRICE] = data["Price_numeric"].apply(lambda x: "Free" if x == 0.0 else f"${x:.2f}")

    return data

def average_reviews(data):
    data[COL_POSITIVE] = data[COL_POSITIVE] / (data[COL_POSITIVE] + data[COL_NEGATIVE]) * 100

    bins = [0, 40, 60, 80, 100]
    labels = ["Mostly negative", "Neutral", "Mostly positive", "Positive"]
    data[COL_REVIEWS] = pd.cut(data[COL_POSITIVE], bins=bins, labels=labels)

    return data

def data_selection(data):
    selected_data = data[[COL_NAME, COL_DEVELOPER, COL_PRICE, COL_REVIEWS, "Price_numeric"]]
    selected_data = selected_data.rename(columns={COL_NAME: "Name", COL_DEVELOPER: "Developer", COL_PRICE: "Price", COL_REVIEWS: "Reviews"})

    return selected_data

def data_filter(selected_data, column, value):
    return selected_data[selected_data[column] == value]

def get_processed_data():
    data = sheet_data()
    data = dollar_converter(data)
    data = average_reviews(data)
    selected_data = data_selection(data)

    return selected_data