str1 = "Hello World"
str2 = "I love Python"
str3 = "This is a string"

set1 = set()
set2 = set()
set3 = set()

for i in range(len(str1)):
    set1.add(str1[i])
for i in range(len(str2)):
    set2.add(str2[i])
for i in range(len(str3)):
    set3.add(str3[i])

new_set1 = set1.difference(set2, set3)
print(new_set1)