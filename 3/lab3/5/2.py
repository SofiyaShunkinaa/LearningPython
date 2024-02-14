dict1 = {"a": 1, "b": 2}
dict1["c"] = 1
print(dict1)

unique = []
for i in dict1.values():
    unique.append(i)
for item in unique:
    if unique.count(item) == 1:
        print(item, end=" ")
print()

dict2 = {
    "a": 1,
    "b": 2,
    "c": [4,5,8,5,2,0,2]
}
count = 0
for item in dict2.values():
    if type(item) == list:
        count = count + 1
print(count)

