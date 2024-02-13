import math

choice = input("What do u want to execute? "
               "1 - /, 2 - *, 3 - -, 4 - +, 5 - //, "
               "6 - **, 7 - sin, 8 - cos, 9 - tan, 10 - sqrt")
match choice:
    case "1":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a/b)
    case "2":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a*b)
    case "3":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a-b)
    case "4":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a+b)
    case "5":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a // b)
    case "6":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a ** b)
    case "7":
        a = int(input("Enter the number: "))
        print(math.sin(a))
    case "8":
        a = int(input("Enter the number: "))
        print(math.cos(a))
    case "9":
        a = int(input("Enter the number: "))
        print(math.tan(a))
    case "10":
        a = int(input("Enter the number: "))
        print(math.sqrt(a))