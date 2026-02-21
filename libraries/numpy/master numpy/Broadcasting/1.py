'''
in this we'll see that how braodcasting is easy to do. 

Problem -> there is some prices in which we have to apply 10% discount 
'''

## 1. using FOR loop

import numpy as np

prices = np.array([100,200,300])
discount = 10

final_prices = []

for price in prices:
    final_price = prices - (prices * discount/100)
    final_prices.append(final_price)

print(final_prices)

##2. using Broadcasting. 

import numpy as np

prices = np.array([100,200,300])
discount = 10

final_prices = prices - (prices * discount/100)

print(final_prices)