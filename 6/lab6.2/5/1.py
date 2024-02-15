import re

f = open('1.txt').readlines()
for date in f:
    if re.match(r'\d{2}.(0[3-5]).\d{4}', date):
        print(date)
