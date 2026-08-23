def avg(lst):
    return sum(lst) / len(lst)
subjects = input("enter subjects separated by comma: ").split(',')
marks = list(map(int,input("enter marks separated by comma: ").split(',')))
student = {
    "subjects": subjects,
    "marks": marks,
    "percentage": round(avg(marks)/100,2)
}
avg_num  = avg(student["marks"])
print(avg_num)
print(student["percentage"])