### MARKERS

##markers - we can use the keyword argument "marker" to emphasize each point with a specified marker:
##marker size or ms - We can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
## marker edge colour - We can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
## marker face color - We can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:



import matplotlib.pyplot as plt
import numpy as np

y_point = np.array([3,8,1,10,7])

plt.plot(y_point , marker = "o" , ms = "16" , mec = "r" , mfc = "hotpink")

plt.show()

