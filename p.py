### graphs of all types :

import matplotlib.pyplot as plt
import numpy as np

# ------- Sample data -------
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

data = np.random.normal(loc=50, scale=10, size=100)   # for histogram & boxplot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
pie_labels = ['Cat 1', 'Cat 2', 'Cat 3']
pie_sizes = [30, 50, 20]

## ===== 1. Bar graph =====
plt.figure()
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')
plt.show()

# ===== 2. Histogram =====
plt.figure()
plt.hist(data, bins=10, color='orange', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# # ===== 3. Pie chart =====
plt.figure()
plt.pie(pie_sizes, labels=pie_labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.axis('equal')  # make it a circle
plt.show()

# # ===== 4. Scatter plot =====
plt.figure()
plt.scatter(x, y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

# # ===== 5. Line graph =====
plt.figure()
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(True)
plt.show()

# # ===== 6. Box plot =====
plt.figure()
plt.boxplot(data)
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
