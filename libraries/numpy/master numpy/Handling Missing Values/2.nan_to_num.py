'''
syntax -> np.nan_to_num(array , nan = value)
agr value nhi di toh default ho kr zero ho jayegi
'''

import numpy as np

arr = np.array([1,2,3,np.nan ,5, np.nan])

clean_arr = np.nan_to_num(arr)
print(clean_arr)

clean_arr = np.nan_to_num(arr,nan=100)
print(clean_arr)