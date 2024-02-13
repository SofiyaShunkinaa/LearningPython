experience = [1, 7, 11, 20]
salary = [500, 1500, 3000, 5000]
arr = zip(experience, salary)

for experience, salary in arr:
    if 5 <= experience <= 10:
        premium = 0.1
    elif 10 < experience <= 15:
        premium = 0.15
    elif experience > 15:
        premium = 0.2
    else:
        premium = 0
    totalSalary = salary + salary*premium
    print("experience: ", experience, "premium: ", premium,
          "total salary: ", totalSalary)