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
    # Inicjalizacja zmiennej xn punktem startowym
    xn = x0
    # Pętla będzie wykonywana dopóki nie zostanie spełniony warunek zakończenia
    while True:
        # Obliczenie wartości funkcji dla aktualnego punktu xn
        fxn = f(xn)
        # Sprawdzenie warunku zakończenia (czy wartość funkcji jest dostatecznie bliska zeru)
        if abs(fxn) < e:
            return xn
        # Obliczenie wartości pochodnej funkcji dla aktualnego punktu xn
        dfxn = df(xn)
        # Sprawdzenie czy pochodna jest różna od zera (aby uniknąć dzielenia przez zero)
        if dfxn == 0:
            return None
        # Obliczenie kolejnego przybliżonego punktu metodą stycznych
        xn = xn - fxn / dfxn

# Punkt startowy to środek przedziału [PI/2, PI]
x0 = (math.pi/2 + math.pi) / 2
e = 0.01

# Wywołanie metody stycznych
rozwiazanie = metoda_stycznych(x0, e)
print(rozwiazanie)
