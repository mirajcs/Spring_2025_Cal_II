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

# Define the rotation about the x-axis
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Compute the surfaces of revolution
Y1 = y1(X) * np.cos(Theta)
Z1 = y1(X) * np.sin(Theta)

Y2 = y2(X) * np.cos(Theta)
Z2 = y2(X) * np.sin(Theta)

# Plot the surfaces
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the outer surface (y = x/2)
ax.plot_surface(X, Y2, Z2, color='blue', alpha=0.6, label='y = x/2')

# Plot the inner surface (y = x^2)
ax.plot_surface(X, Y1, Z1, color='red', alpha=0.6, label='y = x^2')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solid of Revolution: Rotation about the X-axis')

# Show the plot
plt.legend()
plt.show()