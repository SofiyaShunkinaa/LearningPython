dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict2 = {'a': 1, 'b': 2, 'c': 2, 'd': 4, 'e': 5}

values1 = list(dict1.values())
values2 = list(dict2.values())

count = 0
for i in values1:
    if values1.count(i) > 1:
        count = 1
if count == 0:
    print("Unique values")
else:
    print("Not unique values")

count = 0
for i in values2:
    if values2.count(i) > 1:
        count = 1
if count == 0:
    print("Unique values")
else:
    print("Not unique values")
