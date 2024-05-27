import math

import numpy as np

# Definicja funkcji, którą chcemy zintegrować
def f(x):
    return math.sqrt(x+1)

# Metoda trapezów do obliczania całki numerycznej
def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Szerokość każdego trapezu
    integral_approximation = (f(a) + f(b)) / 2.0  # Pierwsza i ostatnia wartość funkcji
    for i in range(1, n):
        integral_approximation += f(a + i * h)  # Sumowanie wartości funkcji wewnątrz przedziału
    integral_approximation *= h  # Mnożenie przez szerokość trapezów
    return integral_approximation  # Zwrócenie przybliżonej wartości całki

# Określenie parametrów
a = 0  # Dolne ograniczenie całkowania
b = 1  # Górne ograniczenie całkowania
n1 = 3  # Liczba trapezów dla pierwszej aproksymacji
n2 = 6  # Liczba trapezów dla drugiej aproksymacji

# Obliczenie dwóch aproksymacji
approximation1 = trapezoidal_rule(a, b, n1)  # Pierwsza aproksymacja
approximation2 = trapezoidal_rule(a, b, n2)  # Druga aproksymacja

# Obliczenie ekstrapolacji Richardsona
richardson_approximation = (4 * approximation2 - approximation1) / 3  # Ekstrapolacja Richardsona

# Obliczenie estymacji błędu
error_estimate = (approximation2 - approximation1) / 3  # Estymacja błędu

# Wydrukowanie wyników
print("Richardson extrapolation approximation:", richardson_approximation)
