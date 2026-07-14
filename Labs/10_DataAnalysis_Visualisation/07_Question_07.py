import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

# Create figure with subplots
plt.figure(figsize=(12,8))

# 1. Line Plot
plt.subplot(2,2,1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")

# 2. Bar Chart
plt.subplot(2,2,2)
plt.bar(x, y)
plt.title("Bar Chart")

# 3. Scatter Plot
plt.subplot(2,2,3)
plt.scatter(x, y)
plt.title("Scatter Plot")

# 4. Pie Chart
plt.subplot(2,2,4)
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()