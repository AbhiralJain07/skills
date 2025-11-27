###   GRID LINES.  ###

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x,y)

# plt.grid()

# plt.show()

### we can specify which line we have to display 

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x,y)

# # plt.grid( axis='x' )
# plt.grid (axis='y')

# plt.show()

###. SETTING LINE PROPERTIES FOR GRID. ###

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.grid(color = "blue" , lw = "2" , ls = "dotted")

plt.show()