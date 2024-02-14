kort1 = (("a", 1), ("b", 2), ("c", 3))

kort = ((3, 1), (8, 2), (0, 3))
a, b, c = kort
list1 = []
list2 = []
list3 = []
for kort in a:
    list1.append(kort)
for kort in b:
    list2.append(kort)
for kort in c:
    list3.append(kort)
print(list1, list2, list3)
