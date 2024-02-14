dict = {
    "f": 1,
    "b": 2,
    "z": 5.5,
    "a": 0
}
values = list(dict.values())
print("max: ", max(values))
print("min: ", min(values))

keys = list(dict.keys())
for key in keys:
    print(key, end=" ")
print()
for value in values:
    print(value, end=" ")

print()
dict2 = {}
dict2['x'] = list(range(11, 22))
dict2['y'] = list(range(21, 31))
dict2['z'] = list(range(31, 41))
print(dict2)

print(dict2['x'][5])
print(dict2['y'][5])
print(dict2['z'][5])
