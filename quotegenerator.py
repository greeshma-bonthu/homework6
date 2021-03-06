import json

f = open("quotes.json", 'r') 


data = json.load()

for node in data:
    dir_name = node["author"].replace(" ", "_")
    print(dir_name)

 