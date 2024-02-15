f = open('2.txt').readlines()
f1 = open('2.1.txt', 'w')
for i in range(len(f)):
    if int(f[i]) % 3 == 0 and int(f[i]) % 7 != 0:
        f1.write(f[i])
