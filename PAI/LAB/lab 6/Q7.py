import numpy as np

rng  = np.random.default_rng(42)

arr = np.array(rng.integers(low=0, high=10, size=10).astype(float))
idx = rng.choice(arr.size, size=5 , replace=False)
arr[idx]= np.nan
nanarrayidx  = np.where(np.isnan(arr))
arr[np.where(np.isnan(arr))] = np.nanmean(arr)
print(arr)
