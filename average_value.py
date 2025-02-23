
import sympy as sp
import scipy.integrate as spi
from fractions import Fraction

def function(x):
    """Define the function to be averaged."""
    return sp.exp(sp.sin(x))*sp.cos(x)  # Example function

def average_value(f, a, b):
    """Calculate the average value of a function over [a, b]."""
    integral, _ = spi.quad(f, a, b)
    return integral / (b - a)
    #return Fraction(avg_value).limit_denominator()

# Define interval
a, b = 0, sp.pi  # Example interval

# Compute average value
avg_value = average_value(function, a, b)
print(f"Average value of the function over [{a}, {b}]: {avg_value}")