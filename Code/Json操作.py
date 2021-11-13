import json
with open("1.json","w") as f:
    content = '[{"name": "jimmy"}]'
    jsonString = json.loads(content)

    json.dump(jsonString,f)



with open("1.json","r") as f:
    data = json.load(f)
print(data[0]) 