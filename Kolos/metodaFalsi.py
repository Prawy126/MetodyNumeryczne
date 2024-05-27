from math import cos

# Definicja funkcji f(x)
def f(x):
    return 3 * x - cos(x) - 1

# Funkcja wartości bezwzględnej
def abs(x):
    if (x >= 0):
        return x
    else:
        return -x

# Funkcja obliczająca pierwiastek metodą falsi
def metoda_falsi(a, b, e):
    # Sprawdzenie założenia
    if (f(a) * f(b) >= 0):
        raise ValueError("Niespełnione założenia - f(a) i f(b) muszą mieć różne znaki.")

    # Poniżej jest zmienna która będzie przechowywać iteracje algorytmu Newtona
    i = 0

    while (True):
        # Obliczanie nowej wartości x0 zgodnie z metodą falsi
        x0 = a - (((b - a) * f(a)) / (f(b) - f(a)))

        i = i + 1

        # Sprawdzanie warunku zbieżności
        if (abs(f(x0)) < e):
            print("Ilość iteracji:", i)
            return x0 # Przerwanie pętli i zwrócenie przybliżoną wartość pierwiastka f(x)
        else:
            # Za nowy przedział [a,b] przyjmujemy tę połówkę [a,x0], [x0,b], w której funkcja zmienia znak
            if (f(x0) * f(a) < 0):
                b = x0
            else:
                a = x0

# Wypisanie wyniku
try:
    print("Metoda falsi")
    wynik = metoda_falsi(0.25, 0.75, 0.00001)
    print("Pierwiastek funkcji:", wynik)
except ValueError as e:
    print("Błąd:", e)
