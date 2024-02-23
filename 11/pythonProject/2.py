import json

try:
    with open('task23   .json', 'r') as f:
        data = json.load(f)

    jsonData = json.dumps(data)
    print(jsonData)
except:
    print('error')
