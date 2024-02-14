string = input("Enter text: ")
new_set = set()
for i in range(len(string)):
    if string[i].islower():
        new_set.add(string[i])
print(sorted(new_set))