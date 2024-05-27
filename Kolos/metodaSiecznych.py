# Definicja funkcji f(x)
def f(x):
    return x**3 + x**2 - 3 * x - 3

# Funkcja wartości bezwzględnej
def abs(x):
    if (x >= 0):
        return x
    else:
        return -x

# Funkcja obliczająca pierwiastek metodą siecznych
def metoda_siecznych(a, b, e):
    # Sprawdzenie założenia
    if (f(a) * f(b) >= 0):
        raise ValueError("Niespełnione założenia - f(a) i f(b) muszą mieć różne znaki.")

    # Poniżej jest zmienna która będzie przechowywać iteracje algorytmu Newtona
    i = 0

    while (True):
        # Obliczanie nowej wartości x0 zgodnie z metodą siecznych
        x0 = b - (f(b) * (b - a)) / (f(b) - f(a))

        i = i + 1

        # Sprawdzanie warunku zbieżności
        if abs(f(x0)) < e:
            print("Ilość iteracji:", i)
            return x0 # Przerwanie pętli i zwrócenie przybliżoną wartość pierwiastka f(x)

        # Przygotowanie wartości dla kolejnej iteracji
        a, b = b, x0

# Wypisanie wyniku
try:
    print("Metoda siecznych")
    wynik = metoda_siecznych(1, 2, 0.0001)
    print("Pierwiastek funkcji:", wynik)
except ValueError as e:
    print("Błąd:", e)
