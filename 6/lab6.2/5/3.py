f = open('3.txt').readlines()
print(f)
for i in range(len(f)):
    if i % 2 == 0:
        if i == 0:
            min = float(f[i])
        else:
            if float(f[i]) < min:
                min = float(f[i])
print("The minimum number is {}".format(min))

