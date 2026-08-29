import random as rd
logs =['INFO', 'ERROR', 'WARNING', 'INFO' , 'ERROR', 'INFO']
transmission = [rd.choice(logs) for i in range(1000)]
total_transmission = {}
for x in logs:
    total_transmission[x] = 0
for x in transmission:
    total_transmission[x] += 1
print(total_transmission)
print(list(dict(sorted(total_transmission.items(), key=lambda item: item[1], reverse=True)).items())[0])