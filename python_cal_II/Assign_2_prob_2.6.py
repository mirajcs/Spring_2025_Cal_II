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

# Define the rotation about the line y = -2
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Shift the y-axis to account for rotation about y = -2
# For rotation about y = -2, the radius is (y + 2)
Y1 = y1(X)  # y = x^2
R1 = Y1 + 2  # Radius for y = x^2
Z1 = R1 * np.sin(Theta)  # z = r * sin(theta)
Y1_rotated = -2 + R1 * np.cos(Theta)  # y = -2 + r * cos(theta)

Y2 = y2(X)  # y = x/2
R2 = Y2 + 2  # Radius for y = x/2
Z2 = R2 * np.sin(Theta)  # z = r * sin(theta)
Y2_rotated = -2 + R2 * np.cos(Theta)  # y = -2 + r * cos(theta)

# Plot the surfaces
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the outer surface (y = x/2)
ax.plot_surface(X, Y2_rotated, Z2, color='blue', alpha=0.6, label='y = x/2')

# Plot the inner surface (y = x^2)
ax.plot_surface(X, Y1_rotated, Z1, color='red', alpha=0.6, label='y = x^2')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solid of Revolution: Rotation about y = -2')

# Show the plot
plt.legend()
plt.show()