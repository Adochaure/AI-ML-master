# JSON (JavaScript Object Notation) is a lightweight data format used to exchange data 
# between programs, APIs, websites, etc. JSON format is very similar to Python 
# dictionaries. 

import json

#use dumps() to convert python object into JSON string

data = {
    "name":"Aditya",
    "age":12,
    "marks":[20,20,203]
}

json_string = json.dumps(data)

print(json_string)


# Converting JSON string to Python 
json_data = '{"name": "Aditya", "age": 12, "marks": [20, 20, 203]}'
python_obj = json.loads(json_data)
print(python_obj["name"])

#Reding  JSON from file -> json.load(f)

import json  
with open("demo.json", "r") as f:  
    data = json.load(f)  
print(data)

#writing json to file -> json.dump()
data_demo = {"name":"mutu swami" , "city":"hogwarts"}

with open("demo.json","w") as f:
    json.dump(data_demo,f,indent=20)