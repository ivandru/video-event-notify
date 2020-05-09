import json

json_file_path = './example.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)
    print(data)