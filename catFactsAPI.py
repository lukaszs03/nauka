import requests
import json
import webbrowser
from pprint import pprint

params = {
    "amount": 5,
}


r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)
a = requests.get("https://randombig.cat/roar.json")

try:
    content = r.json()
    image = [a.json()]
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    for cat in content:
        print(cat["text"])
    for url in image:
        webbrowser.open_new_tab(url["url"])
