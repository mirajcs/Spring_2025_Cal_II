import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variable
x = sp.Symbol('x')

# Define the bounding functions
y1 = x**2  # Lower function
y2 = x/2   # Upper function

# Solve for intersection points
sol = sp.solve(y1 - y2, x)
a, b = sol  # Extract the limits

# Define the radius of circular cross-sections
r = (y2 - y1) / 2

# Set up the volume integral
volume_integral = sp.integrate(sp.pi * r**2, (x, a, b))

# Display the result
sp.pprint(volume_integral)

# Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Enable interactive rotation
ax.view_init(elev=20, azim=30)

# Generate x values
x_vals = np.linspace(float(a), float(b), 30)

# Store min/max values for axis limits
x_min, x_max = float(a), float(b)
y_min, y_max = 0, 0
z_min, z_max = 0, 0

# Plot circular cross-sections
for x_val in x_vals:
    radius = float(((x_val / 2) - x_val**2) / 2)
    center_y = float((x_val / 2 + x_val**2) / 2)
    if radius > 0:
        theta = np.linspace(0, 2 * np.pi, 100)
        z = radius * np.cos(theta)
        y = center_y + radius * np.sin(theta)
        ax.plot(x_val * np.ones_like(y), y, z, 'b')
        
        # Update limits
        y_min, y_max = min(y_min, min(y)), max(y_max, max(y))
        z_min, z_max = min(z_min, min(z)), max(z_max, max(z))

# Set equal scale for all axes
max_range = max(x_max - x_min, y_max - y_min, z_max - z_min) / 2
mid_x, mid_y, mid_z = (x_max + x_min) / 2, (y_max + y_min) / 2, (z_max + z_min) / 2
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Solid with Circular Cross-Sections')

plt.show()
