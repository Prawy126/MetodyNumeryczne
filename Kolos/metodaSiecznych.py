from sympy import *

x = Symbol('x')

E = 0.0001  # Przybliżenie
a = 1  # Początek przedziału
b = 2  # Koniec przedziału


def f(x):
    return x ** 3 + x ** 2 - 3 * x - 3


def df1(x1):  # Pierwsza pochodna f
    return diff(f(x), x).subs(x, x1)


def df2(x1):  # Druga pochodna f
    return diff(f(x), x, x).subs(x, x1)


def siecznych(a, b, E):
    global x1

    if f(a) * f(b) < 0:  # Założenie 1: Funkcja zmienia znak na krańcach przedziału
        i = 0  # Licznik iteracji

        if df1(a) * df2(a) > 0:  # Założenie 2: Wybór punktu startowego
            x0 = a
            x1 = b
        else:
            x0 = b
            x1 = a

        xn = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))  # Pierwsze przybliżenie

        while abs(f(xn)) > E:  # Dopóki wartość funkcji w punkcie nie spełnia dokładności E
            temp = xn - (f(xn) * (xn - x1)) / (f(xn) - f(x1))  # x_n+1
            x1 = xn
            xn = temp

            i += 1

    print("Szukany pierwiastek to: " + str(xn))  # Wyświetlenie wyniku
    print("Liczba iteracji: " + str(i))  # Wyświetlenie liczby iteracji


siecznych(a, b, E)
