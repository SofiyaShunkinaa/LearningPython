def calculate_sum(*numbers):
    for number in numbers:
        if type(number) == float or type(number) == int:
            print(f'The summary is {sum(numbers)}')
            return sum(numbers)
        else:
            print("Invalid input")
            return None


calculate_sum(1, 5, 25)
calculate_sum("d", 5)
calculate_sum(1.5, 6, 2.5, 1)