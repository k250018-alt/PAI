import random as rd
arr = [rd.randint(1, 10) for i in range(10)]
dic ={}
for i in arr:
    dic[i] = False
print(arr)
print(dic)
for i in dic:
    dic[i] = True
    for j in dic:
        if not dic[j] and i+j == 10:
            print(i,",",j)
