import random as rd

lst = [rd.randint(1,100) for x in range(100) ]

def find_duplicates(lst):
    seen = set()
    duplicate = set()
    for x in lst:
        if x in seen:
            duplicate.add(x)
        else:
            seen.add(x)
    return duplicate,seen
duplicate,seen = find_duplicates(lst)
print("seen items")
print(seen)
print(len(seen))
print("duplicate items")
print(duplicate)
print(len(duplicate))