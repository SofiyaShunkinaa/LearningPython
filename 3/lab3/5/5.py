dict2 = {
    "f": '1',
    "b": '2',
    "z": '5.5',
    "a": '0'
}
sortdesc = sorted(dict2.items())
print(sortdesc)

for i in dict2.values():
    print(i, end=" ")
print()
for i in dict2.keys():
    print(i, end=" ")
print()
for key, value in dict2.items():
    print(key, value, end="  ")
print()

for item in dict2:
    if "." in dict2[item] :
        dict2[item] = float(dict2[item])
    else:
        dict2[item] = int(dict2[item])
print(dict2)