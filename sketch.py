import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return (x - 3)**2

def g(x):
    return np.ones_like(x)  # g(x) = 1 for all x

# Define the interval
x = np.linspace(2, 5, 400)  # Generate 400 points between 2 and 5

# Compute function values
y_f = f(x)
y_g = g(x)

# Plot the functions
plt.figure(figsize=(8, 5))
plt.plot(x, y_f, label=r"$f(x) = (x-3)^2$", color='blue')
plt.plot(x, y_g, label=r"$g(x) = 1$", color='red', linestyle='dashed')

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of $f(x) = (x-3)^2$ and $g(x) = 1$")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()