kort = 1, 2, 3
list = list(kort)
new_item = 20
list.append(new_item)
new_kort = tuple(list)
print(new_kort)

print(f"It's tuple ({kort[0]}, {kort[1]}, {kort[2]})")
