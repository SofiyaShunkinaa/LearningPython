students = {"Sofiya": 9, "Ann": 6, "John": 8, "David": 1}
sorted_students1 = sorted(students.items(), key=lambda item: item[1])
print(sorted_students1)
sorted_students2 = sorted(students.items(), key=lambda item: item[1], reverse=True)
print(sorted_students2)

dict1 = {"a": 1, "b": 5}
dict2 = {"b": 2, "d":3}
dicts = dict()
for key, value in dict1.items():
    dicts[key] = value
for key, value in dict2.items():
    if key in dicts:
        dicts[key] += value
    else:
        dicts[key] = value
print(dicts)

if len(dicts) > 1:
    print("There are more than one key")
    