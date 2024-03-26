# Definicja funkcji f(x) = x^3 + x^2 - 3x - 3
def f(x):
    return x**3 + x**2 - 3*x - 3

# Implementacja metody siecznych
def metoda_siecznych(x0, x1, E):
    """
    x0, x1: punkty startowe
    E: dokładność
    """
    # Pętla wykonuje się dopóki różnica między x1 a x0 jest większa lub równa E
    while abs(x1 - x0) >= E:
        # Obliczenie wartości funkcji dla punktów x0 i x1
        f_x0 = f(x0)
        f_x1 = f(x1)
        # Sprawdzenie, czy wartości funkcji dla punktów x0 i x1 są równe
        if f_x0 == f_x1:
            break
        # Wyznaczenie nowej przybliżonej wartości pierwiastka
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        # Aktualizacja punktów x0 i x1 dla kolejnej iteracji
        x0, x1 = x1, x2
    # Zwrócenie przybliżonej wartości pierwiastka
    return x1

# Początkowe punkty i dokładność
x0 = 1
x1 = 2
E = 0.0001

# Wywołanie metody siecznych
rozwiazanie = metoda_siecznych(x0, x1, E)
print(rozwiazanie)
