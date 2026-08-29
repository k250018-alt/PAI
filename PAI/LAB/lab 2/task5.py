import random as rd
import string as st
employee_id = [rd.choice(st.ascii_uppercase)+str(rd.randint(1, 100)) for x in range(10000)]
employee_database ={}
for x in employee_id:
    name = ''.join(rd.choice(st.ascii_letters) for i in range(10))
    department = ''.join(rd.choice(st.ascii_letters) for i in range(10))
    salary = rd.randint(1, 10000)
    job = rd.choice(st.ascii_letters)
    employee_database[x] = [name, department, salary, job]
print(employee_database)
find_employee = input('Enter employee id: ')
print(employee_database[find_employee] if find_employee in employee_database else None)
change_salary = input('Enter salary: ')
employee_database[find_employee][2] = change_salary
add_employee = input('Enter employee id: ')
new_emp_salary = input('Enter new employee salary: ')
new_emp_name = input('Enter new employee name: ')
new_emp_department = input('Enter new employee department: ')
new_emp_job = input('Enter new employee job: ')
if add_employee in employee_database:
    print("already an employee")
else:
    employee_database[add_employee] = [new_emp_name,new_emp_department,new_emp_salary,new_emp_job]
print(employee_database)
remove_employee = input('Enter employee id: ')
if remove_employee in employee_database:
    del employee_database[remove_employee]
else:
    print("employee not found")
print(employee_database)