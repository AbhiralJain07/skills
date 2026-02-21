#bahut saare arrays ko combine krna ho chahe vertically krna ho chahe horizontally

#syntax-
# vstack()- for vertically or row wise
# hstack() - for horizontally or coloumn wise

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))