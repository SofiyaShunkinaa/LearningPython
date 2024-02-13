for i in range(7):
    if i % 2 == 0:
        for j in range(11):
            print("+", end="")
        print("")
    else:
        for j in range(11):
            if j % 5 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

