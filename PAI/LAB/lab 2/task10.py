employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]
employees_database ={}
for employee in employees:
    employees_database[employee[0]] = employee[1:]
total= 0
for employee in employees:
    total += employees_database[employee[0]][-1]
avg = total/len(employees)
highest = list(dict(sorted(employees_database.items(), key=lambda item: item[1][-1], reverse=True)).values())[0][-1]
departments= {}
for employee in employees:
    departments[employee[2]] =0
for employee in employees:
    departments[employee[2]] +=1
print(employees)
print(employees_database)
print(avg)
print(highest)
print(departments)

