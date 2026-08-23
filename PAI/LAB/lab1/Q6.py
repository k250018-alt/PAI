subjects = input("enter subjects separated by comma: ").split(',')
marks = list(map(int,input("enter marks separated by comma: ").split(',')))
student = {
    "subjects": subjects,
    "marks": marks
}
def avg(lst):
    return sum(lst)/len(lst)
avg_num  = avg(student["marks"])
best_subject,best_marks = max(student.items(),key =lambda item:item[1])
print(best_subject)
print(best_marks)
print(avg_num)