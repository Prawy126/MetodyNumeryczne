# MetodyNumeryczne

To repozytorium jest poświęcone implementacjom algorytmów matematycznych w języku Python

### Tematy:
- [horner wyliczanie wartosci w danym punkcie](https://github.com/Prawy126/MetodyNumeryczne/tree/main/horner)
    - kod:

```python
def horner(tablica, x):
    wynik = tablica[0]
    for i in range(1, len(tablica)):
        wynik = wynik * x + tablica[i]
    return wynik

stopien_wielomianu = int(input("Podaj stopień wielomianu: "))
tablica = []

print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(stopien_wielomianu + 1):
    y = int(input())
    tablica.append(y)

x = int(input("Podaj wartość x: "))

print("Oto twoja tablica współczynników:", tablica)
wynik = horner(tablica, x)
print("Wynik wielomianu dla x =", x, "wynosi", wynik)
```
- [horner dzielenie wielomianu](https://github.com/Prawy126/MetodyNumeryczne/tree/main/horner2)
  - kod:

```python
def hornerDzielenie(tablica, x, rzad):
    wynik = []
    for i in range(rzad):
        wartosc = tablica[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)
    return wynik
rzad = int(input("Proszę podać rząd wielomianu: "))
tablica = []
print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(rzad + 1):
    y = int(input())
    tablica.append(y)

x = int(input("Proszę podać liczbę przez, którą będziemy dzielić: "))

wynik = hornerDzielenie(tablica, x, rzad)
```

 - [bisekcja](https://github.com/Prawy126/MetodyNumeryczne/tree/main/bisekcja)
    - kod:

```python
def bisekcja(func, a, b, error_accept):
    def f(x):
        return func(x)

    if f(a) * f(b) >= 0:
        raise ValueError("Założenia bisekcji nie zostały spełnione - f(a) i f(b) muszą mieć różne znaki.")

    while abs(b - a) > error_accept:
        c = (a + b) / 2
        if f(c) == 0:
            break  # Znaleziono dokładny pierwiastek
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

```

 - [Metoda stycznych](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_stycznych)
    - cod:
 
 ```python

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

```
- [Metoda siecznych](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_siecznych)
   - cod:

```python
# Definicja funkcji f(x) = x^3 + x^2 - 3x - 3
def f(x):
    return x**3 + x**2 - 3*x - 3

# Implementacja metody siecznych
def metoda_siecznych(x0, x1, E):
    """
    x0, x1: punkty startowe
    E: dokładność
    """
    while abs(x1 - x0) >= E:
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x0 == f_x1:
            break
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    return x1

# Początkowe punkty i dokładność
x0 = 1
x1 = 2
E = 0.0001

# Wywołanie metody siecznych
rozwiazanie = metoda_siecznych(x0, x1, E)
print(rozwiazanie)

```
- [Metoda falsi](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_stycznych)
  - cod:

```python
# Definicja funkcji f(x) = 3x - cos(x) - 1
import math
def f(x):
    return 3 * x - math.cos(x) - 1


# Implementacja metody regula falsi
def metoda_regula_falsi(x0, x1, e):
    """
    x0, x1: punkty startowe
    e: dokładność
    """
    f_x0 = f(x0)
    f_x1 = f(x1)

    if f_x0 * f_x1 > 0:
        return None  # Funkcja musi mieć różne znaki na końcach przedziału

    while abs(f_x1 - f_x0) > e:
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)  # Obliczenie nowego przybliżenia
        f_x2 = f(x2)

        if abs(f_x2) < e:
            return x2

        # Aktualizacja punktów x0 i x1
        if f_x2 * f_x0 < 0:
            x1 = x2
            f_x1 = f_x2
        else:
            x0 = x2
            f_x0 = f_x2

    return (x0 + x1) / 2


# Początkowe punkty i dokładność
x0 = 0.25
x1 = 0.75
e = 0.00001

# Wywołanie metody regula falsi
rozwiazanie = metoda_regula_falsi(x0, x1, e)
print(rozwiazanie)

```

- Metoda prostokątów
    - kod:

```python

import matplotlib.pyplot as plt
import numpy as np


# Definicja funkcji do zcałkowania
def f(x):
    return 0.06 * x ** 2 + 2


# Całkowanie numeryczne - metoda prostokątów
def metoda_prostokatow(a, b, n):
    dx = (b - a) / n  # Szerokość każdego prostokąta
    area = 0  # Inicjalizacja sumy powierzchni
    for i in range(n):
        area += f(a + i * dx) * dx  # Sumowanie powierzchni prostokątów
    return area


# Obliczanie błędu
def oblicz_blad(n, area):
    # Dokładna wartość całki
    dokladna_wartosc = (1 / 3) * (b ** 3 * 0.06 + 2 * b) - (1 / 3) * (a ** 3 * 0.06 + 2 * a)
    blad = abs(dokladna_wartosc - area)
    return blad


# Definicja granic całkowania i liczby prostokątów
a = 1
b = 4
n = 1000  # Liczba prostokątów, im większa, tym dokładniejszy wynik

# Obliczenie powierzchni za pomocą metody prostokątów
area = metoda_prostokatow(a, b, n)

# Obliczenie błędu
error = oblicz_blad(n, area)

# Rysowanie funkcji i prostokątów dla ilustracji
x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y, 'b', linewidth=2)

# Dodawanie prostokątów
for i in range(n):
    plt.gca().add_patch(plt.Rectangle((a + i * (b - a) / n, 0), (b - a) / n, f(a + i * (b - a) / n),
                                      edgecolor='gray', facecolor='lightgray', linewidth=1))

plt.fill_between(x, y, color='lightblue', alpha=0.5)

# Dodawanie tekstu z obliczoną powierzchnią i błędem
plt.text(2.5, 8, f'Powierzchnia = {area:.2f}', fontsize=12, ha='center')
plt.text(2.5, 7.5, f'Błąd = {error:.2f}', fontsize=12, ha='center')

plt.title('Całkowanie - Metoda prostokątów')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

print("Obliczona powierzchnia:", area)

```

- Metoda trapezów
  - cod:

```python

import numpy as np

def f(x):
    return x**2 + 3

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral_approximation = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral_approximation += f(a + i * h)
    integral_approximation *= h
    return integral_approximation

# Define the parameters
a = 2  # lower limit of integration
b = 5  # upper limit of integration
n1 = 3  # number of trapezoids for first approximation
n2 = 6  # number of trapezoids for second approximation

# Calculate the two approximations
approximation1 = trapezoidal_rule(a, b, n1)
approximation2 = trapezoidal_rule(a, b, n2)

# Calculate Richardson extrapolation
richardson_approximation = (4 * approximation2 - approximation1) / 3

# Calculate error estimation
error_estimate = (approximation2 - approximation1) / 3

print("Richardson extrapolation approximation:", richardson_approximation)

```

- Metoda praboli
  - cod:
  
```python

import math
import numpy as np

ITERACJE = 0
DX = 10 ** -7

def pochodna(f):
    return lambda x: (f(x + DX) - f(x)) / DX

def cSimpson(f, start, stop, divs):
    h = (stop - start) / divs
    s = 0
    ans = 0
    for i in range(1, divs):
        x = start + i * h
        s += f(x - h / 2)
        ans += f(x)
    s += f(stop - h / 2)
    ans = (h / 6) * (f(start) + f(stop) + 2 * ans + 4 * s)
    return ans

def error_estimate(f, start, stop, divs1, divs2):
    approx1 = cSimpson(f, start, stop, divs1)
    approx2 = cSimpson(f, start, stop, divs2)
    richardson_approx = (4 * approx2 - approx1) / 3
    error = abs(richardson_approx - approx2)
    return error


f1 = lambda x: (x**2 + x + 1) / (x**5 + 6*x**4 + x**3 + 2*x + 2)
upper_bound = 1
lower_bound = 0
divs1 = 8
divs2 = 1

print("Wynik:", cSimpson(f1, lower_bound, upper_bound, divs1))


```

- Interpolacja
    - cod:

```python

# from scipy.interpolate import lagrange
# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import symbols, expand
#
# # Define the data points
# x_points = np.array([1, 2, 3])
# y_points = np.array([5, 7, 6])
#
# # Perform Lagrange interpolation
# lagrange_poly = lagrange(x_points, y_points)
#
# # Convert the polynomial coefficients into a list
# lagrange_coeffs = lagrange_poly.coefficients.tolist()
#
# # Create the symbolic variable
# x = symbols('x')
#
# # Construct the Lagrange polynomial expression
# lagrange_poly_sympy = expand(sum(coeff * x**i for i, coeff in enumerate(lagrange_coeffs)))
#
# # Display the polynomial
# print(lagrange_poly_sympy)
# """"
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀ ⠈⢻⣿⣿⡄⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
# ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
# ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
# ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
# ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿
# ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
# ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
# ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# """""
import numpy as np
import matplotlib.pyplot as plt

# Definicja punktów
x_points = np.array([1, 2, 3])
y_points = np.array([5, 7, 6])

def lagrange(x, x_points, y_points):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        li = 1
        for j in range(n):
            if i != j:
                xj = x_points[j]
                li = (x - xj) / (xi - xj)
        total += yi * li
    return total

# Zakres i rozdzielczość wykresu
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
y_range = [lagrange(x, x_points, y_points) for x in x_range]

# Wypisanie równania Lagrange'a
def lagrange_polynomial(x_points, y_points):
    x = symbols('x')
    lagrange_poly = 0
    for i in range(len(x_points)):
        term = 1
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        lagrange_poly += term * y_points[i]
    return expand(lagrange_poly)

from sympy import symbols, expand

x = symbols('x')
lagrange_poly = lagrange_polynomial(x_points, y_points)
print("Lagrange Polynomial:")
print(lagrange_poly)

# Rysowanie wykresu
plt.plot(x_range, y_range, label='Interpolating Polynomial')
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.title('Lagrange Polynomial Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

```
