f = open('5.txt', 'r')
f1 = open('5.1.txt', 'w')
signs = '.,:!?-;'
string = f.read()
for i in range(len(string)):
    if string[i] in signs:
        f1.write(string[i])
f.close()
f1.close()
