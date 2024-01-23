import json

#file_open = open("test.json")
#data = json.load(file_open)
with open("test.json") as f:
    data = json.load(f)
print(data)