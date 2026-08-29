import random as rd
students = [rd.randint(1,100) for x in range(1000)]
courses = {"A":[],"B":[]}
for x in students:
    i = rd.randint(1,2)
    if i == 1:
        courses["A"] = courses["A"] + [x]
    if i == 2:
        courses["B"] = courses["B"] + [x]
a_unique = set(courses["A"])
b_unique = set(courses["B"])
student_in_both = a_unique & b_unique
print(student_in_both)
std_in_a = a_unique - b_unique
std_in_b = b_unique - a_unique
print(std_in_a)
print(std_in_b)
unique_in_both = list(std_in_a) + list(std_in_b)
print(unique_in_both)
