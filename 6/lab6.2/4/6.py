f = open('6.txt').readlines()
count = 0
sum = 0
for i in range(len(f)):
    sum += int(f[i].strip())
    count += 1
print("The sum of the ", count, " numbers is: ", sum)
