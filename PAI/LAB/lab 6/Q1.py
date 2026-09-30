import numpy as np
rng = np.random.default_rng(42)
marks = np.array(rng.integers(30, 100, (10, 7)))
print("marks")
print(marks)
totals = marks.sum(axis=1)
avg  = totals/7
print("student total")
print(totals)
print("student avg")
print(avg)
avg_sub = marks.mean(axis=0)
print("subject avg")
print(avg_sub)
passedall = (marks >= 50).all(axis = 1)
result = np.where(passedall ,"pass" ,"fail")
print("result")
print(result)



