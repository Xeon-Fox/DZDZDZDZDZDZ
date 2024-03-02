import json

data = {
    "surname": "Алексей",
    "name": "Алесей",
    "dumb": True,
    "gender": "MALE"
}

with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)

json_string = json.dumps(data)
print(json_string)


parsed_data = json.loads(json_string)
print(parsed_data)


with open("data.json", "w", encoding="utf8") as file:
    json.dump(data, file)

