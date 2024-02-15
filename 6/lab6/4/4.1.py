f = open('text1.txt').readlines()
K = 4
print(f)

if K in range(len(f)):
    f.pop(K)
else:
    print('Not found')
print(f)
f1 = open('text1.txt', 'w')
f1.writelines(f)
f1.close()
