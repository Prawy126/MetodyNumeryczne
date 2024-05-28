from sympy import *
x = Symbol('x')
import math

E = 0.01  # Przybliżenie
a = math.pi/2  # Początek przedziału
b = math.pi  # Koniec przedziału

def f(x):   # Funkcja
    return sin(x) - 0.5 * x

def df1(x1): # Pierwsza pochodna f
    return diff(f(x), x).subs(x, x1)

def df2(x1): # Druga pochodna f
    return diff(f(x), x, x).subs(x, x1)

def metodaStycznych(a, b, e):
    if f(a) * f(b) < 0:  # Założenie 1: Sprawdzenie, czy istnieje pierwiastek w przedziale [a, b]
        if f(a) * df2(a) > 0:  # Założenie 2: Wybór punktu startowego
            x0 = a
        else:
            x0 = b

        i = 0  # Licznik iteracji
        xn = x0 - f(x0) / df1(x0)  # Pierwsze przybliżenie

        while abs(f(xn)) > e:  # Dopóki wartość funkcji w punkcie nie spełnia dokładności e
            xn = xn - f(xn) / df1(xn)  # Metoda stycznych
            i += 1

    print("Szukany pierwiastek: " + str(xn))  # Wyświetlenie wyniku
    print("Liczba wszystkich iteracji: " + str(i))  # Wyświetlenie liczby iteracji

metodaStycznych(a, b, E)
