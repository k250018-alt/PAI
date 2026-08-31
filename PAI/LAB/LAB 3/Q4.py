import random as rd
lst = [ rd.randint(1,2) for i in range(1000) ]

def majority_elements(lt):
    counts = {}
    for x in lt:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for i in counts:
        if counts[i] > len(lt)/2:
            print( i ,"is a majority element")
print(lst)
majority_elements(lst)