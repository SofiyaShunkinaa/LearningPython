string = input("Enter numbers: ")
new_set = set()
for i in range(len(string)):
    new_set.add(string[i])
print(sorted(new_set))