class Cliente:
    def __init__(self):
        pass

import json
with open("Aula_12/arquivo.json", "w") as file:
    json.dump({"video1": "feifeifkef"}, file)

with open("Aula_12/arquivo.json", "r") as file:
    caralhoooo: dict = json.load(file)
print(caralhoooo)