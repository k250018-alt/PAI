import numpy as np
rng  = np.random.default_rng(42)
sensors = np.array(rng.integers(low=1, high=5, size=(10,4)))
print(sensors)
avg = sensors.mean(axis=1)
mn = sensors.min(axis=1)
mx = sensors.max(axis=1)
print("mean")
print(avg)
print("min")
print(mn)
print("max")
print(mx)
print("highest avg")
print(avg.max())
mask = sensors >= 3
result = sensors[mask]
print(result)


