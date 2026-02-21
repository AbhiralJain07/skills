#isme 2 element ko add krte hai

#syntax - 
#np.concatenate((array1, array2),axis =0)

import numpy as np
arr_1 = np.array([[1,2]])
arr_2 = np.array([[4,9]])
new_arr = np.concatenate((arr_1,arr_2),axis = 0)
print(new_arr)