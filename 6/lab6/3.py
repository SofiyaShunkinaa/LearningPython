import os

number = int(input("Enter a number: "))
if os.path.isdir('PRIM'):
    for i in range(number):
        os.mkdir(f'C:/git/LearningPython/6/lab6/PRIM/prim{i+1}')

for i in range(number):
    os.rmdir(f'C:/git/LearningPython/6/lab6/PRIM/prim{i+1}')
