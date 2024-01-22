import json

x= '{"name":"John", "age":30, "City": "New York"}'
# parse x
y = json.loads(x)
print(y["age"])
print(y.get("name"))

a = {"name":"John", "age":30, "City": "New York"}
print(type(a))
b = json.dumps(a)
print(b)
print(type(b))
c = json.loads(b)
print(c.get("City"))

file = open("test.json")
data = json.load(file)
data_file = data[0]
data_in_json = data_file.get("data")
print(data_in_json)
dis_name = data_in_json.get("factSheet").get("description")
print(dis_name)

file = open("test.json")
data = json.load(file)
data_file = data[0]
data_in_json = data_file.get("data")
print(data_in_json)
factSheet_in_json = data_in_json.get("factSheet")
print(factSheet_in_json)
permissions_in_json = factSheet_in_json.get("permissions")
print(permissions_in_json)
completion_in_json = permissions_in_json.get("completion").get("create").get("read").get("update").get("delete").get("self")
print(completion_in_json)



#tags_in_json = permissions_in_json.get("tags")
#print(tags_in_json)
