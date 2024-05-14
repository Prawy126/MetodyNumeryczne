import math  # Importuje moduł matematyczny.
from sympy import symbols, diff  # Importuje funkcje symbols i diff z modułu sympy.

# Definiujemy zmienną symboliczną
x = symbols('x')  # Tworzy zmienną symboliczną x.

def wyborX0(rownanie, x_val):
    # Oblicza wartość funkcji oraz jej pochodnej w punkcie x_val.
    f = rownanie(x_val)
    fdiff = diff(rownanie(x), x).subs(x, x_val)
    return f * fdiff  # Zwraca iloczyn wartości funkcji i jej pochodnej w punkcie x_val.

def styczne(rownanie, dokladnosc, dolnyPrzedzial, gornyPrzedzial):
    # Sprawdza, czy funkcja zmienia znak na podanym przedziale.
    a = rownanie(dolnyPrzedzial)
    b = rownanie(gornyPrzedzial)
    assert a * b < 0, "Funkcja nie zmienia znaku na przedziale"

    # Wybiera punkt startowy x0 w zależności od znaku iloczynu f(x) i f'(x).
    if wyborX0(rownanie, dolnyPrzedzial) > 0:
        x0 = dolnyPrzedzial
    elif wyborX0(rownanie, gornyPrzedzial) > 0:
        x0 = gornyPrzedzial
    else:
        raise ValueError("Nie można wybrać x0")

    # Pętla iteracyjna metody Newtona-Raphsona.
    while True:
        fx0 = rownanie(x0)
        fprime_x0 = float(diff(rownanie(x), x).subs(x, x0))  # Oblicza wartość pochodnej w punkcie x0.
        x1 = x0 - fx0 / fprime_x0  # Oblicza nowe przybliżenie miejsca zerowego.

        # Sprawdza warunek dokładności, zwraca wynik jeśli jest spełniony.
        m = min(abs(float(diff(rownanie(x), x, 2).subs(x, dolnyPrzedzial))),
                abs(float(diff(rownanie(x), x, 2).subs(x, gornyPrzedzial))))
        if abs(rownanie(x1)) / m <= dokladnosc:
            return x1
        else:
            x0 = x1  # Aktualizuje przybliżenie punktu startowego.

# Definiuje funkcję przykładową.
rownanie = lambda x: x ** 3 - 2 * x ** 2 - 3 * x - 5
# Wywołuje funkcję styczne i drukuje wynik.
print(styczne(rownanie, 0.0001, 3, 4))
