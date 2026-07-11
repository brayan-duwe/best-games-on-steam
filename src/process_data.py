import json
import pandas as pd


with open("data/raw_data.json", "r") as content:
    data = json.load(content)


df = pd.json_normalize(list(data.values()))
print(df)