import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x - 1

# Define the number of subintervals
n_intervals = 5
x_intervals = np.linspace(-6, 4, n_intervals + 1)  # n+1 points to get n subintervals

# Right-endpoint values
x_right = x_intervals[1:]  # Taking rightmost values in each subinterval
y_right = f(x_right)

# Compute Riemann sum
dx = (x_intervals[1] - x_intervals[0])  # Width of each subinterval
riemann_sum = np.sum(y_right * dx)

# Plot function
x_values = np.linspace(-6, 4, 100)
y_values = f(x_values)

plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label=r"$f(x) = x - 1$", color='blue')
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.grid(True, linestyle='--', alpha=0.6)

# Plot rectangles for Right Riemann sum
for i in range(n_intervals):
    plt.bar(x_intervals[i], y_right[i], width=dx, align='edge', alpha=0.4, edgecolor='red', color='orange')

# Labels and title
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Right Riemann Sum Approximation")
plt.legend(["Function", "Riemann Rectangles"])
plt.show()

# Display the computed Riemann sum
print("Right Riemann Sum:", riemann_sum)