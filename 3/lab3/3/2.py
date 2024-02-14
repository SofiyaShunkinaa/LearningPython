import math
list = [3, 5, 8, 1, 2, 9, 6, 0.5]

for i in range(len(list)):
    if i == 0:
        min_index = i
        max_index = i
        min = list[i]
        max = list[i]
    else:
        if list[i] > max:
            max_index = i
            max = list[i]
        if list[i] < min:
            min_index = i
            min = list[i]
if min_index < max_index:
    print(math.prod(list[min_index:max_index+1]))
else:
    print(math.prod(list[max_index:min_index + 1]))

