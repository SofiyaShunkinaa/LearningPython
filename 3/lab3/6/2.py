string = input("Enter text: ")
nums = set()
symbols = set()
for i in string:
    if i.isdigit():
        nums.add(int(i))
    elif i == "+" or i == "-" or i == "*":
        symbols.add(i)
print("Count of numbers is: ", len(nums))
print("Count of symbols is: ", len(symbols))
