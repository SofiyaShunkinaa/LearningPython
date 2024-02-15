f = open('text.txt').readlines()

f1 = open('text.txt', 'w')
K = 3
for line in f:
    if len(line) > K:
        f1.write(line[K:])
    else:
        f1.write("\n")



