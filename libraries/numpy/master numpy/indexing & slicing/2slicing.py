'''
slicing

array = [start , stop , step]

arr[start:end] , start to end -1

negative step -1, reverse 

'''

import numpy as np

arr = np.array([10,22,43,56,58,26])

print(arr[1:4]) #index 1 to 3 
print(arr[:3]) #index 0 to 2
print(arr[::2]) #every second element
print(arr[::-1])