import math

res1 = (((float(input("x: "))**2 + 12*float(input("c: ")) -
         math.sqrt(float(input("x: "))))/(4*float(input("v: ")))) -
        pow(float(input("x: ")), 4))

res2 = (math.sin(float(input("b: ")*2)) + math.sqrt(3*(float(input("v: ")))) -
        44*math.cos(float(input("x: "))*4))

res3 = (float(input("x: ")) % 2 + math.sqrt(3*(float(input("v: ")))) -
        44*math.cos(4* float(input("x: "))))

print(res1, res2, res3, sep='-', end='!!!!')

