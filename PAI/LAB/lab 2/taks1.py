import random
lst = []
student = {}
for i in range(10):
    student = {"marks" : [random.randint(1,100) for x in range(5)],"name" : "student" + str(i+1)}
    lst.append(student)
marks = list(map(int, input("Enter the marks: ").split()))
name = input("Enter the student's name: ")
found = False
for student in lst:
    if student["name"] == "student1":
        student["marks"] = marks
        found = True
if not found:
    temp = {"marks" : marks,"name" : name}
    lst.append(temp)
total=0
for student in lst:
    total += sum(student["marks"])
    student["total"] = sum(student["marks"])
    student["average"] = student["total"]/len(student["marks"])
total_avg = total / len(lst)
print(lst)
above_avg = []
for student in lst:
    if student["total"] >= total_avg:
        above_avg.append(student)
print(total_avg)
print(above_avg)
highest_student = max(lst, key = lambda x: x["total"])
print(highest_student)