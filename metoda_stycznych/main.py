import math
from sympy import symbols, diff

# Definiujemy zmienną symboliczną
x = symbols('x')


def wyborX0(rownanie, x_val):
    f = rownanie(x_val)
    fdiff = diff(rownanie(x), x).subs(x, x_val)
    return f * fdiff


def styczne(rownanie, dokladnosc, dolnyPrzedzial, gornyPrzedzial):
    a = rownanie(dolnyPrzedzial)
    b = rownanie(gornyPrzedzial)

    assert a * b < 0, "Funkcja nie zmienia znaku na przedziale"

    if wyborX0(rownanie, dolnyPrzedzial) > 0:
        x0 = dolnyPrzedzial
    elif wyborX0(rownanie, gornyPrzedzial) > 0:
        x0 = gornyPrzedzial
    else:
        raise ValueError("Nie można wybrać x0")

    while True:
        fx0 = rownanie(x0)
        fprime_x0 = float(diff(rownanie(x), x).subs(x, x0))
        x1 = x0 - fx0 / fprime_x0

        m = min(abs(float(diff(rownanie(x), x, 2).subs(x, dolnyPrzedzial))),
                abs(float(diff(rownanie(x), x, 2).subs(x, gornyPrzedzial))))
        if abs(rownanie(x1)) / m <= dokladnosc:
            return x1
        else:
            x0 = x1


rownanie = lambda x: x ** 3 - 2 * x ** 2 - 3 * x - 5
print(styczne(rownanie, 0.0001, 3, 4))
