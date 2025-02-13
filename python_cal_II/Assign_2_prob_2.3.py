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

# Define the rotation about the y-axis
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Compute the surfaces of revolution
# For rotation about the y-axis, x becomes the radius
Y1 = y1(X)  # y = x^2
Z1 = X * np.sin(Theta)  # z = r * sin(theta)
X1 = X * np.cos(Theta)  # x = r * cos(theta)

Y2 = y2(X)  # y = x/2
Z2 = X * np.sin(Theta)  # z = r * sin(theta)
X2 = X * np.cos(Theta)  # x = r * cos(theta)

# Plot the surfaces
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the outer surface (y = x/2)
ax.plot_surface(X2, Y2, Z2, color='blue', alpha=0.6, label='y = x/2')

# Plot the inner surface (y = x^2)
ax.plot_surface(X1, Y1, Z1, color='red', alpha=0.6, label='y = x^2')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solid of Revolution: Rotation about the Y-axis')

# Show the plot
plt.legend()
plt.show()