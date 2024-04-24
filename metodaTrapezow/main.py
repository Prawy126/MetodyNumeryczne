import numpy as np

def f(x):
    return x**2 + 3

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral_approximation = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral_approximation += f(a + i * h)
    integral_approximation *= h
    return integral_approximation

# Define the parameters
a = 2  # lower limit of integration
b = 5  # upper limit of integration
n1 = 3  # number of trapezoids for first approximation
n2 = 6  # number of trapezoids for second approximation

# Calculate the two approximations
approximation1 = trapezoidal_rule(a, b, n1)
approximation2 = trapezoidal_rule(a, b, n2)

# Calculate Richardson extrapolation
richardson_approximation = (4 * approximation2 - approximation1) / 3

# Calculate error estimation
error_estimate = (approximation2 - approximation1) / 3

print("Richardson extrapolation approximation:", richardson_approximation)
