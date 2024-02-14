import re

email = input("Enter your email: ")
result = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', email)
if result is None:
    print("Invalid email adress")
else:
    print("Valid email adress")
