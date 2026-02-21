'''

flattening arrays -:
1. ravel() -> returns view
2. flatten() -> returns copy

'''

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())