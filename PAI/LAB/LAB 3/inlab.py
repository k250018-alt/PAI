from functools import reduce
lst = [1,2,3,4,5]
mult =[]
temp = []
for x in range(len(lst)):
    if x ==0 :
        temp = lst[x+1]
    if x == len(lst)-1:
        temp = lst[:-1]
    else:
        temp = lst[x+1:] + lst[:x]
    mult.append(reduce(lambda x,y: x*y, temp))
print(lst)
print(mult)