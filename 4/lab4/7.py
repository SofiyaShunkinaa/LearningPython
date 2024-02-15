def print_user_info(name, age, city="Минск"):
    if type(name) == str and type(age) == int and type(city) == str:
        print(f"Name: {name}, Age: {age}, City: {city}")
    else:
        print("Invalid Name or Age")


print_user_info("Sofi", 19)
print_user_info(city="Berlin", age=19, name="Mary")
print_user_info("Sofi", "19")
