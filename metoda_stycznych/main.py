import math

# Definicja funkcji f(x) = sin(x) - 0.5x
def f(x):
    return math.sin(x) - 0.5 * x

# Definicja pochodnej funkcji f'(x) = cos(x) - 0.5
def df(x):
    return math.cos(x) - 0.5

# Implementacja metody stycznych
def metoda_stycznych(x0, e):
    """
    x0 -  punkt startowy
    e - dokładność
    """
    xn = x0
    while True:
        fxn = f(xn)
        if abs(fxn) < e:
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            return None
        xn = xn - fxn / dfxn

# Punkt startowy to środek przedziału [PI/2, PI]
x0 = (math.pi/2 + math.pi) / 2
e = 0.01

# Wywołanie metody stycznych
rozwiazanie = metoda_stycznych(x0, e)
print(rozwiazanie)
