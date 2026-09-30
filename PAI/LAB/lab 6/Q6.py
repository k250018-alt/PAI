import numpy as np

rng1 = np.random.default_rng(42)

martix = np.array(rng1.integers(low=0, high=1000, size=10))
print("martix seed 42")
print(martix)
print("mean")
print(martix.mean())
print("median")
print(np.median(martix))
print("standard deviation")
print(np.std(martix))
inside = (martix >= martix.mean() -martix.std())&(martix <= martix.mean() +martix.std())
percentage = inside.sum()/martix.size *100
print("percentage")
print(percentage)

rng1 = np.random.default_rng(72)

martix = np.array(rng1.integers(low=0, high=1000, size=10))
print("martix seed 42")
print(martix)
print("mean")
print(martix.mean())
print("median")
print(np.median(martix))
print("standard deviation")
print(np.std(martix))
inside = (martix >= martix.mean() -martix.std())&(martix <= martix.mean() +martix.std())
percentage = inside.sum()/martix.size *100
print("percentage")
print(percentage)