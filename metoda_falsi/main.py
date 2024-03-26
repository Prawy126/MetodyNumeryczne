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
    # Obliczenie wartości funkcji dla punktów startowych x0 i x1
    f_x0 = f(x0)
    f_x1 = f(x1)

    # Sprawdzenie, czy funkcja ma różne znaki na końcach przedziału
    if f_x0 * f_x1 > 0:
        return None  # Jeśli nie, to metoda nie może być zastosowana

    # Pętla wykonuje się dopóki różnica między wartościami funkcji dla punktów x0 i x1 jest większa od zadanej dokładności e
    while abs(f_x1 - f_x0) > e:
        # Obliczenie nowego przybliżenia korzystając z reguły falsi
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        f_x2 = f(x2)

        # Sprawdzenie, czy wartość funkcji w nowym punkcie spełnia warunek zakończenia
        if abs(f_x2) < e:
            return x2

        # Aktualizacja punktów x0 i x1 na podstawie wartości funkcji w punkcie x2
        if f_x2 * f_x0 < 0:
            x1 = x2
            f_x1 = f_x2
        else:
            x0 = x2
            f_x0 = f_x2

    # Zwrócenie przybliżonego miejsca zerowego, gdy różnica między x0 i x1 jest mniejsza od e
    return (x0 + x1) / 2

# Początkowe punkty i dokładność
x0 = 0.25
x1 = 0.75
e = 0.00001

# Wywołanie metody regula falsi
rozwiazanie = metoda_regula_falsi(x0, x1, e)
print(rozwiazanie)
