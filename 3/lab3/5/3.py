dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dicts = {**dict1, **dict2}
print(dicts)
sortedDict = sorted(dicts.items(), key=lambda item: item[1], reverse=True)
print(sortedDict)

dict3 = {"a": 1, "b": [1, 3, 8]}
for item in dict3.values():
    if type(item) == list:
        item.clear()
print(dict3)
