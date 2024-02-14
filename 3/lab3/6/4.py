str1 = "Hello World"
str2 = "I love Python"
str3 = "love"

set1 = set()
set2 = set()
set3 = set()

for i in range(len(str1)):
    set1.add(str1[i])
for i in range(len(str2)):
    set2.add(str2[i])
for i in range(len(str3)):
    set3.add(str3[i])

merged_set = set1.union(set2)
print(set3.issubset(merged_set))
