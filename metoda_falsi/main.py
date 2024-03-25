# Definicja funkcji f(x) = 3x - cos(x) - 1
import math
def f(x):
    return 3 * x - math.cos(x) - 1


# Implementacja metody regula falsi
def metoda_regula_falsi(x0, x1, e):
    """
    x0, x1: punkty startowe
    e: dokładność
    """
    f_x0 = f(x0)
    f_x1 = f(x1)

    if f_x0 * f_x1 > 0:
        return None  # Funkcja musi mieć różne znaki na końcach przedziału

    while abs(f_x1 - f_x0) > e:
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)  # Obliczenie nowego przybliżenia
        f_x2 = f(x2)

        if abs(f_x2) < e:
            return x2

        # Aktualizacja punktów x0 i x1
        if f_x2 * f_x0 < 0:
            x1 = x2
            f_x1 = f_x2
        else:
            x0 = x2
            f_x0 = f_x2

    return (x0 + x1) / 2


# Początkowe punkty i dokładność
x0 = 0.25
x1 = 0.75
e = 0.00001

# Wywołanie metody regula falsi
rozwiazanie = metoda_regula_falsi(x0, x1, e)
print(rozwiazanie)