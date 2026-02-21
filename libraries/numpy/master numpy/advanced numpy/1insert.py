'''
syntax - 
np.insert(array, index , value , axis= none)

array = original array
index - jis position pr apn insert krna chahte hai
value - kya value insert krna chahte h 
axis = 0 iska matlb h data ko row wise insert krna hai
axis = 1 iska matlb h data ko coloumn wise insert krna hai

'''

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr , 2 , 100)
print(new_arr)