import numpy as np

# Dane punktów
x_points = np.array([0, 3, 6,9, 12])
y_points = np.array([4, 5, 4, 1,2])

# Stopień wielomianu
degree = 3

# Użycie polyfit do znalezienia współczynników wielomianu
coefficients = np.polyfit(x_points, y_points, degree)

# Użycie poly1d do utworzenia funkcji wielomianowej
p = np.poly1d(coefficients)

# Wyświetlenie współczynników wielomianu
print("Współczynniki wielomianu:", p)
#Wielomian aproksymujący:
#       3          2
#0.01852 x - 0.3492 x + 1.357 x + 3.914