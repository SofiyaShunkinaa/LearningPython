f = open('4.txt').readlines()
g = open('even.txt', 'w')
h = open('odd.txt', 'w')

for line in f:
    if float(line) % 2 == 0:
        g.write(line)
    else:
        h.write(line)
