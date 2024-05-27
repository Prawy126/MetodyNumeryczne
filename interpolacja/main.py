import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand

# Definicja punktów danych
x_points = np.array([1, 2, 3])  # Wartości x
y_points = np.array([5, 7, 6])  # Wartości odpowiadające y

# Funkcja obliczająca wielomian interpolacyjny Lagrange'a
def lagrange(x, x_points, y_points):
    total = 0  # Inicjalizacja sumy
    n = len(x_points)  # Liczba punktów danych
    for i in range(n):
        xi, yi = x_points[i], y_points[i]  # Aktualny punkt danych
        li = 1  # Inicjalizacja wielomianu Lagrange'a dla danego i
        for j in range(n):
            if i != j:
                xj = x_points[j]  # Inny punkt danych
                li *= (x - xj) / (xi - xj)  # Wielomian Lagrange'a dla danego i
        total += yi * li  # Dodanie do sumy iloczynu wielomianu i odpowiadającej wartości y
    return total  # Zwrócenie wartości wielomianu interpolacyjnego w punkcie x

# Zakres i rozdzielczość wykresu
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)  # Zakres wartości x
y_range = [lagrange(x, x_points, y_points) for x in x_range]  # Wartości y dla danego wielomianu interpolacyjnego

# Wypisanie równania Lagrange'a
def lagrange_polynomial(x_points, y_points):
    x = symbols('x')  # Symbol zmiennoprzecinkowej x
    lagrange_poly = 0  # Inicjalizacja wielomianu Lagrange'a
    for i in range(len(x_points)):
        term = 1  # Inicjalizacja pojedynczego składnika wielomianu
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])  # Obliczenie składnika wielomianu
        lagrange_poly += term * y_points[i]  # Dodanie składnika wielomianu do wielomianu Lagrange'a
    return expand(lagrange_poly)  # Rozwinięcie wielomianu Lagrange'a

x = symbols('x')  # Symbol zmiennoprzecinkowej x
lagrange_poly = lagrange_polynomial(x_points, y_points)  # Obliczenie wielomianu Lagrange'a
print("Lagrange Polynomial:")
print(lagrange_poly)  # Wydrukowanie wielomianu Lagrange'a

# Rysowanie wykresu
plt.plot(x_range, y_range, label='Interpolating Polynomial')  # Rysowanie wielomianu interpolacyjnego
plt.scatter(x_points, y_points, color='red', label='Data Points')  # Rysowanie punktów danych
plt.title('Lagrange Polynomial Interpolation')  # Tytuł wykresu
plt.xlabel('x')  # Etykieta osi x
plt.ylabel('y')  # Etykieta osi y
plt.legend()  # Dodanie legendy
plt.grid(True)  # Włączenie siatki
plt.show()  # Wyświetlenie wykresu