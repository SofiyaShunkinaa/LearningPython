f1 = open('f1.txt').readlines()
f2 = open('f2.txt').readlines()
f = open('f1.txt', 'w')

if len(f1) == len(f2):
    for i in range(len(f1)):
        f.write(f1[i].strip() + f2[i])
elif len(f1) > len(f2):
    for i in range(len(f2)):
        f.write(f1[i].strip() + f2[i])
    f.write('\n')
    for i in range(len(f1) - len(f2)+1, len(f1)):
        f.write(f1[i])
f.close()
