# from scipy.interpolate import lagrange
# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import symbols, expand
#
# # Define the data points
# x_points = np.array([1, 2, 3])
# y_points = np.array([5, 7, 6])
#
# # Perform Lagrange interpolation
# lagrange_poly = lagrange(x_points, y_points)
#
# # Convert the polynomial coefficients into a list
# lagrange_coeffs = lagrange_poly.coefficients.tolist()
#
# # Create the symbolic variable
# x = symbols('x')
#
# # Construct the Lagrange polynomial expression
# lagrange_poly_sympy = expand(sum(coeff * x**i for i, coeff in enumerate(lagrange_coeffs)))
#
# # Display the polynomial
# print(lagrange_poly_sympy)
# """"
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀ ⠈⢻⣿⣿⡄⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
# ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
# ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
# ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
# ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿
# ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
# ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
# ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# """""
import numpy as np
import matplotlib.pyplot as plt

# Definicja punktów
x_points = np.array([1, 2, 3])
y_points = np.array([5, 7, 6])

def lagrange(x, x_points, y_points):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        li = 1
        for j in range(n):
            if i != j:
                xj = x_points[j]
                li = (x - xj) / (xi - xj)
        total += yi * li
    return total

# Zakres i rozdzielczość wykresu
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
y_range = [lagrange(x, x_points, y_points) for x in x_range]

# Wypisanie równania Lagrange'a
def lagrange_polynomial(x_points, y_points):
    x = symbols('x')
    lagrange_poly = 0
    for i in range(len(x_points)):
        term = 1
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        lagrange_poly += term * y_points[i]
    return expand(lagrange_poly)

from sympy import symbols, expand

x = symbols('x')
lagrange_poly = lagrange_polynomial(x_points, y_points)
print("Lagrange Polynomial:")
print(lagrange_poly)

# Rysowanie wykresu
plt.plot(x_range, y_range, label='Interpolating Polynomial')
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.title('Lagrange Polynomial Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
