# Convert objet to json file
import json
data = {
    'name':'Suri',
    "Age": 25,
    "Study": "Btech",
    "Address": {
        "city":"Vijayawada","state":"Andhra Pradesh"
    },
    "branches" :['cse','ece','mech','civil']
}
print("Object Format:",data)

json_format = json.dumps(data, indent=4)
print("json_format:",json_format)