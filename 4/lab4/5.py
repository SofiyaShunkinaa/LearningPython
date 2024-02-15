def FlattenList(list):
    new_list = []
    for sublist in list:
        for subitem in sublist:
            new_list.append(subitem)
    return new_list


print(FlattenList([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]))

