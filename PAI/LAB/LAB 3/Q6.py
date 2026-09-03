import random as rd
def find_k_freq(k,lst):
    dic = {}
    for item in lst:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    filtered= list(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))
    top_k =[]
    for i in range(k):
        top_k.append(filtered[i])
    return top_k
lst = [rd.randint(1,100) for i in range(1000)]
k = int(input("Enter the value of k: "))
print("the top ",k, "numbers in list : ",find_k_freq(k,lst))
