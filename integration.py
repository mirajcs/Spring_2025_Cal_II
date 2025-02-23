import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define the function to integrate
f = 62.4*sp.pi*(144-x**2)**2  # Example function

# Define the limits
a, b = -12, 12  # Limits of integration

# Compute the definite integral
result = sp.integrate(f, (x, a, b))
print("Symbolic Definite Integral:", result)