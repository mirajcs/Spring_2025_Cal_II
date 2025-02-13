import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the functions
def y1(x):
    return x**2

def y2(x):
    return x / 2

# Define the range of x values
x = np.linspace(0, 0.5, 100)

# Define the rotation about the line x = -1
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Shift the x-axis to account for rotation about x = -1
radius = X + 1  # Distance from x = -1 to the curve

# Compute the surfaces of revolution
# For rotation about x = -1, the radius is (x + 1)
Y1 = y1(X)  # y = x^2
Z1 = radius * np.sin(Theta)  # z = r * sin(theta)
X1 = -1 + radius * np.cos(Theta)  # x = -1 + r * cos(theta)

Y2 = y2(X)  # y = x/2
Z2 = radius * np.sin(Theta)  # z = r * sin(theta)
X2 = -1 + radius * np.cos(Theta)  # x = -1 + r * cos(theta)

# Plot the surfaces
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the outer surface (y = x/2)
ax.plot_surface(X2, Y2, Z2, color='yellow', alpha=0.6, label='y = x/2')

# Plot the inner surface (y = x^2)
ax.plot_surface(X1, Y1, Z1, color='red', alpha=0.6, label='y = x^2')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solid of Revolution: Rotation about x = -1')

# Show the plot
plt.legend()
plt.show()