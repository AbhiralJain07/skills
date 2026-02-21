import numpy as np

arr = np.array([1,2,3,np.inf,5, -np.inf])

print(np.isinf(arr))

fresh_array = np.nan_to_num(arr , posinf=10 , neginf=30)

print(fresh_array)