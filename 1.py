### PLOTTING. - ## the plot function is used to draw points (markers) on the plot

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,5])
ypoints = np.array([0,200])

plt.plot(xpoints, ypoints)
plt.show()


## the plot function is used to draw points (markers) on the plot

## drawing Multiple Points on the graph
import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1,2,6,8])
y_points = np.array([3,8,1,10])

plt.plot(x_points , y_points)
plt.show()

## default x points
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10, 5, 7])

plt.plot(y_points)
plt.show()

