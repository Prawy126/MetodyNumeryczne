import math
import numpy as np

ITERACJE = 0  # Liczba iteracji, obecnie nieużywana
DX = 10 ** -7  # Mała wartość zmiany x, używana do obliczania pochodnej

# Funkcja zwracająca funkcję, która oblicza przybliżoną pochodną funkcji f w punkcie x
def pochodna(f):
    return lambda x: (f(x + DX) - f(x)) / DX

# Metoda Simpsona do całkowania numerycznego
def cSimpson(f, start, stop, divs):
    h = (stop - start) / divs  # Szerokość podziału
    s = 0  # Suma dla środkowych punktów
    ans = 0  # Suma dla wszystkich punktów
    for i in range(1, divs):
        x = start + i * h  # Wartość x dla aktualnego przedziału
        s += f(x - h / 2)  # Wartość funkcji w środku przedziału
        ans += f(x)  # Wartość funkcji na krańcach przedziału
    s += f(stop - h / 2)  # Wartość funkcji w środku ostatniego przedziału
    ans = (h / 6) * (f(start) + f(stop) + 2 * ans + 4 * s)  # Obliczenie całki metodą Simpsona
    return ans

# Funkcja do oszacowania błędu przybliżenia
def error_estimate(f, start, stop, divs1, divs2):
    approx1 = cSimpson(f, start, stop, divs1)  # Aproksymacja pierwsza
    approx2 = cSimpson(f, start, stop, divs2)  # Aproksymacja druga
    richardson_approx = (4 * approx2 - approx1) / 3  # Aproksymacja Richardsona
    error = abs(richardson_approx - approx2)  # Obliczenie błędu
    return error

# Definicja funkcji, której całkę chcemy policzyć
f1 = lambda x: (x**2 + x + 1) / (x**5 + 6*x**4 + x**3 + 2*x + 2)
upper_bound = 1  # Górna granica całkowania
lower_bound = 0  # Dolna granica całkowania
divs1 = 8  # Liczba podziałów dla pierwszego przybliżenia
divs2 = 1  # Liczba podziałów dla drugiego przybliżenia

# Wydrukowanie wyniku całkowania dla funkcji f1
print("Wynik:", cSimpson(f1, lower_bound, upper_bound, divs1))
