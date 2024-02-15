def calculate_average(*numbers):
    for number in numbers:
        if type(number) == float or type(number) == int:
            print(f'The average is {sum(numbers)/len(numbers)}')
            return sum(numbers)/len(numbers)
        else:
            print("Invalid input")
            return None


calculate_average(1, 5, 25)
calculate_average("d", 5)
calculate_average(1.5, 6, 2.5, 1)
