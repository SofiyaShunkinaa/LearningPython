x = 10
y = 15

if x < y:
    print('yes')
elif x > y:
    x, y = y, x
    print('x: ', x, ", y: ", y)
else:
    print('x X5: ', str(x)*5, ", y X5: ", str(y)*5)
