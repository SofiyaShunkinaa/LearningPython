name = str(input('What is your name? '))  # string
age = int(input('How old are you? '))  # int
weight = float(input('How much do you weigh? '))  # float
is_student = bool(input('Are u a student? '))  # bool
height = int(input('How tall are you? '))  # int
print("Hi", name, ",your age is ", age,
      ", your weight is ", weight, ", your height is ", height,
      "u are a student: ", is_student)

print(type(name))
print(type(age))
print(type(weight), type(is_student), type(height))

