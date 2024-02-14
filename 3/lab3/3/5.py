list = [3, -5, -8, 1, -2, 9, 6, -0.5]
k = 0
new_list = []
for i in range(len(list)):
    if list[i] < k:
        new_list.append(list[i])
print(sorted(new_list))
