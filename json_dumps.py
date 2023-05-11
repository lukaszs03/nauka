"""
json.dumps(data) - postac stringowa json
json.dump(data, nameOfFile, ensure_ascii=False) - zapisuje do pliku w postaci json
"""

import json

film = {
    "title" : "Syn ciemności",
    "release_year" : 2019,
    "won_oscar" : False,
    "actors" : ("Sample Actor1", "Sample Actor2"),
    "budget" : None,
    "credits" : {
        "director" : "Sample Director",
        "writer" : "Sample Writer",
        "animator" : "Sample Animator"
    }
}

encodedFilm = json.dumps(film, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)