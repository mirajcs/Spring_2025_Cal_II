import numpy as np
import matplotlib.pyplot as plt

# Define the x values from x=1 to a large number to show the decay
x = np.linspace(0.01, 15, 1000)
y = 1 / x**2

# Create the figure and axis
fig, ax = plt.subplots()

# Fill the region under the curve
ax.fill_between(x, y, where=(x >= 1), color='skyblue', alpha=1, label=r"$S$: Region under $y = \frac{1}{x^2}$, $x > 1$")

# Plot the curve itself
ax.plot(x, y, 'b', label=r"$y = \frac{1}{x^2}$")

# Add vertical line at x = 1
ax.axvline(x=1, color='k', linestyle='--', label=r"$x = 1$")

# Add labels and legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Region S: Under $y = 1/x^2$, $x > 1$')
ax.legend()

# Set the y-limit to better show the shape
ax.set_ylim(0, 1.4)

# Show grid
ax.grid(True)

# Display the plot
plt.show()