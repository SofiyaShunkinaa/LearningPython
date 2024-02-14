import statistics
import itertools

dict2 = {
    "a": 4,
    "b": 6,
    "c": 5
}
print("b" in dict2.keys())

my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = list(itertools.product(my_dict['1'], my_dict['2']))

for combination in combinations:
    print(''.join(combination), end=" ")
print()

numbers = []
for i in dict2.values():
    numbers.append(i)
number = statistics.mean(numbers)
for item in dict2:
    dict2[item] = number

print(dict2)
