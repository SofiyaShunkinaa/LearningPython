K = 2
f = open("text.txt").readlines()
lines = 0

for line in f:
    lines += 1
print(lines)
print(f)

for i in range(K):
    f.pop(-1)
print(f)
f1 = open("text.txt", 'w')
f1.writelines(f)
f1.close()