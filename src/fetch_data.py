import requests
import json

api_url = "https://steamspy.com/api.php?request=all"


response = requests.get(api_url)

if response.status_code == 200:
    new_data = response.json()

    with open("data/raw_data.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)
        print("Data appended to fetch_data.json file.")
else:
    print("Failed t retrieve data from the API. Status code:", response.status_code)
