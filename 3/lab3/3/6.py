list = [3, -5, -8, 1, -2, 9, 6, -0.5]
k = 0
negative_list = []
positive_list = []
for i in range(len(list)):
    if list[i] < k:
        negative_list.append(list[i])
    else:
        positive_list.append(list[i])
negative_list = negative_list + positive_list
print(negative_list)
