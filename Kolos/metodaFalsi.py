from sympy import *
x = Symbol('x')

E = 0.00001  # Dokładność
a = 0.25  # Lewa krawędź przedziału początkowego
b = 0.75  # Prawa krawędź przedziału początkowego

def f(x):
    return 3*x - cos(x) - 1

def df1(x1): # Pierwsza pochodna f
    return diff(f(x), x).subs(x, x1)

def df2(x1): # Druga pochodna f
    return diff(f(x), x, x).subs(x, x1)

def metodaFalsi(a, b, E):
    if f(a) * f(b) < 0:  # Założenie 1: Sprawdzenie, czy istnieje pierwiastek w przedziale [a, b]
        i = 0  # Licznik iteracji
        xn = a - f(a) * (b - a) / (f(b) - f(a)) # Pierwsze przybliżenie
        fxn = f(xn)
        if df1(a) * df2(a) > 0: # Założenie 2: Wybór punktu startowego
            x0 = a
        else:
            x0 = b
        fx0 = f(x0)
        while abs(fxn) > E:  # Dopóki wartość funkcji w punkcie nie spełnia dokładności E
            xn = xn - fxn * (x0 - xn) / (fx0 - fxn)  # Metoda Falsi
            fxn = f(xn)
            i += 1
    print("Szukany pierwiastek: " + str(xn))  # Wyświetlenie wyniku
    print("Liczba iteracji: " + str(i))  # Wyświetlenie liczby iteracji

metodaFalsi(a, b, E)
