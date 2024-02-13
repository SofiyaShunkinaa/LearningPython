for i in range(1, 7):
    if i==1 or i==6:
        for j in range(10):
            print("+", end="")
        print("")
    else:
        for j in range(10):
            if j==0 or j==9:
                print("+", end="")
            else:
                print(" ", end="")
        print("")
