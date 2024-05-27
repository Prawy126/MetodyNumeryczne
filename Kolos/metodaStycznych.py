import sympy as sp

x = sp.Symbol('x')

# Definicje funkcji f(x) i pochodnych 1 i 2 stopnia
def f(x):
    return sp.sin(x) - (x / 2)

def f1(x1):
    return sp.diff(f(x), x, x).subs(x, x1)

def f2(x1):
    return sp.diff(f1(x), x, x).subs(x, x1)

# Funkcja wartości bezwzględnej
def abs(x):
    if (x >= 0):
        return x
    else:
        return -x

# Funkcja obliczająca pierwiastek metodą stycznych Newtona-Raphsona
def metoda_stycznych(a, b, e):
    # Sprawdzenie założenia
    if (f(a) * f(b) <= 0 and f1(a) * f2(b) >= 0):
        raise ValueError("Niespełnione założenia - f(a) i f(b) muszą mieć różne znaki.")

    # Wybór początkowego punktu
    if (f(a) * f2(a) > 0):
        x0 = a
    else:
        x0 = b

    # Poniżej jest zmienna która będzie przechowywać iteracje algorytmu Newtona
    i = 0

    while (True):
        # Sprawdzanie warunku zbieżności
        if (abs(f(x0)) < e):
            print("Ilość iteracji:", i)
            return x0 # Przerwanie pętli i zwrócenie przybliżoną wartość pierwiastka f(x)
        else:
            # Obliczanie nowej wartości x0 zgodnie z metodą stycznych
            x0 = float(x0) - (float(f(x0)) / float(f1(x0)))
            i = i + 1

# Wypisanie wyniku
try:
    print("Metoda stycznych Newtona-Raphsona")
    wynik = metoda_stycznych(sp.pi / 2, sp.pi, 0.01)
    print("Pierwiastek funkcji:", wynik)
except ValueError as e:
    print("Błąd:", e)
