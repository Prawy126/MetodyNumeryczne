# Definicja funkcji f(x) = x^3 + x^2 - 3x - 3
def f(x):
    return x**3-4*x-12

# Implementacja metody siecznych
def metoda_siecznych(x0, x1, E):
    """
    x0, x1: punkty startowe
    E: dokładność
    """
    while abs(x1 - x0) >= E:
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x0 == f_x1:
            break
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    return x1

# Początkowe punkty i dokładność
x0 = 2
x1 = 3
E = 0.0001

# Wywołanie metody siecznych
rozwiazanie = metoda_siecznych(x0, x1, E)
print(rozwiazanie)
