import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the variable
x = sp.Symbol('x')

# Define the bounding functions
y1 = x**2  # Lower function
y2 = x/2   # Upper function

# Solve for intersection points
sol = sp.solve(y1 - y2, x)
a, b = sol  # Extract the limits

# Define the base length of equilateral triangle cross-sections
s = y2 - y1

# Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Enable interactive rotation
ax.view_init(elev=20, azim=30)

# Generate x values
x_vals = np.linspace(float(a), float(b), 20)

# Store min/max values for axis limits
x_min, x_max = float(a), float(b)
y_min, y_max = 0, 0
z_min, z_max = 0, 0

# Plot equilateral triangle cross-sections
for x_val in x_vals:
    base_length = float((x_val / 2) - x_val**2)
    if base_length > 0:
        height = (np.sqrt(3) / 2) * base_length
        
        # Define triangle vertices
        v1 = [x_val, x_val**2, 0]
        v2 = [x_val, x_val/2, 0]
        v3 = [x_val, (x_val/2+x_val**2)/2, height]
        
        # Create triangular face
        triangle = np.array([v1, v2, v3])
        ax.add_collection3d(Poly3DCollection([triangle], color='b', alpha=0.6))
        
        # Update limits
        y_min, y_max = min(y_min, -base_length / 2), max(y_max, base_length / 2)
        z_min, z_max = min(z_min, 0), max(z_max, height)

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
ax.set_title('Solid with Equilateral Triangle Cross-Sections')

plt.show()
