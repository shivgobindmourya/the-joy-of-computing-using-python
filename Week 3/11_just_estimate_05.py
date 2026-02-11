"""
JUST ESTIMATE – PART 05
Plotting Crowd Estimates using Matplotlib

This script demonstrates:
- Line Plot
- Different markers
- Axis labeling
- Title
"""

import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Basic line plot
plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Basic Line Plot Example")

plt.show()


# Different style examples

# Red dots
plt.plot(x, y, "ro")
plt.title("Red Dots")
plt.show()

# Blue squares
plt.plot(x, y, "bs")
plt.title("Blue Squares")
plt.show()

# Green triangles
plt.plot(x, y, "g^")
plt.title("Green Triangles")
plt.show()
