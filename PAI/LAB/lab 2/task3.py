import random as rd
transaction_id = [rd.randint(1,100) for x in range(10000)]
print(transaction_id)
unique_id = list(set(transaction_id))
print(unique_id)