import json

json_file = "program.json"

with open(json_file, "r") as file1:
    data_value = file1.read()

    parsed_json = json.loads(data_value)

    print("Presenting Programming  Languages :" , parsed_json)
