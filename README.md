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

- [Metoda prostokątów](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_prostokatow)
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

- [Metoda trapezów](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_trapezow)
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

- [Metoda praboli](https://github.com/Prawy126/MetodyNumeryczne/tree/main/metoda_prostokatow)
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

- [Interpolacja](https://github.com/Prawy126/MetodyNumeryczne/tree/main/interpolacja)
    - cod:

```python


import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand

# Definicja punktów danych
x_points = np.array([1, 2, 3])  # Wartości x
y_points = np.array([5, 7, 6])  # Wartości odpowiadające y

# Funkcja obliczająca wielomian interpolacyjny Lagrange'a
def lagrange(x, x_points, y_points):
    total = 0  # Inicjalizacja sumy
    n = len(x_points)  # Liczba punktów danych
    for i in range(n):
        xi, yi = x_points[i], y_points[i]  # Aktualny punkt danych
        li = 1  # Inicjalizacja wielomianu Lagrange'a dla danego i
        for j in range(n):
            if i != j:
                xj = x_points[j]  # Inny punkt danych
                li *= (x - xj) / (xi - xj)  # Wielomian Lagrange'a dla danego i
        total += yi * li  # Dodanie do sumy iloczynu wielomianu i odpowiadającej wartości y
    return total  # Zwrócenie wartości wielomianu interpolacyjnego w punkcie x

# Zakres i rozdzielczość wykresu
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)  # Zakres wartości x
y_range = [lagrange(x, x_points, y_points) for x in x_range]  # Wartości y dla danego wielomianu interpolacyjnego

# Wypisanie równania Lagrange'a
def lagrange_polynomial(x_points, y_points):
    x = symbols('x')  # Symbol zmiennoprzecinkowej x
    lagrange_poly = 0  # Inicjalizacja wielomianu Lagrange'a
    for i in range(len(x_points)):
        term = 1  # Inicjalizacja pojedynczego składnika wielomianu
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])  # Obliczenie składnika wielomianu
        lagrange_poly += term * y_points[i]  # Dodanie składnika wielomianu do wielomianu Lagrange'a
    return expand(lagrange_poly)  # Rozwinięcie wielomianu Lagrange'a

x = symbols('x')  # Symbol zmiennoprzecinkowej x
lagrange_poly = lagrange_polynomial(x_points, y_points)  # Obliczenie wielomianu Lagrange'a
print("Lagrange Polynomial:")
print(lagrange_poly)  # Wydrukowanie wielomianu Lagrange'a

# Rysowanie wykresu
plt.plot(x_range, y_range, label='Interpolating Polynomial')  # Rysowanie wielomianu interpolacyjnego
plt.scatter(x_points, y_points, color='red', label='Data Points')  # Rysowanie punktów danych
plt.title('Lagrange Polynomial Interpolation')  # Tytuł wykresu
plt.xlabel('x')  # Etykieta osi x
plt.ylabel('y')  # Etykieta osi y
plt.legend()  # Dodanie legendy
plt.grid(True)  # Włączenie siatki
plt.show()  # Wyświetlenie wykresu

```

- [Aproksymacja](https://github.com/Prawy126/MetodyNumeryczne/tree/main/aproksymacja)
    - cod:

```python

import numpy as np

# Dane punktów
x_points = np.array([0, 3, 6, 12])
y_points = np.array([4, 5, 4, 2])

# Stopień wielomianu
degree = 3

# Użycie polyfit do znalezienia współczynników wielomianu
coefficients = np.polyfit(x_points, y_points, degree)

# Użycie poly1d do utworzenia funkcji wielomianowej
p = np.poly1d(coefficients)

# Wyświetlenie współczynników wielomianu
print("Współczynniki wielomianu:", p)
#Wielomian aproksymujący:
#       3          2
#0.041 x - 0.5966 x + 6.599 x + 7.453

```

- [Eliminacja Gaussa](https://github.com/Prawy126/MetodyNumeryczne/tree/main/eliminacjaGaussa)
    - cod:

```python

import numpy as np

# Definicja macierzy A i wektora b jako float
A = np.array([
    [3, 0, 6],       # Definicja macierzy A
    [1, 2, 8],
    [4, 5, -2]
], dtype=float)
b = np.array([-12, -12, 39], dtype=float)  # Definicja wektora b

# Funkcja wykonująca eliminację Gaussa z wyborem elementu głównego
def gaussian_elimination_with_pivoting(A, b):
    n = len(b)  # Liczba równań/rozmiar macierzy
    # Tworzymy macierz rozszerzoną poprzez dołączenie wektora b jako nowej kolumny
    Ab = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):

        # Sprawdzamy założenia
        determinant = np.linalg.det(A)
        assert determinant != 0, "Wyznacznik macierzy nie jest różny od zera. Macierz jest osobliwa i nie można jej rozwiązać."
        # Wybór elementu głównego w kolumnie i
        max_row = np.argmax(np.abs(Ab[i:, i])) + i  # Znajdujemy indeks maksymalnego elementu
        # Zamiana wierszy, aby maksymalny element był na pozycji głównej
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # Upewniamy się, że element główny nie jest zerowy
        assert Ab[i, i] != 0, "Matrix is singular and cannot be solved."


        # Eliminacja Gaussa
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]  # Współczynnik do eliminacji
            Ab[j, i:] -= factor * Ab[i, i:]  # Eliminacja wiersza

    # Rozwiązywanie układu równań metodą wstecznej substytucji
    x = np.zeros(n)  # Inicjalizacja wektora rozwiązania
    for i in range(n - 1, -1, -1):  # Iteracja od ostatniego wiersza do pierwszego
        # Obliczenie i-tej współrzędnej wektora rozwiązania
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]

    return x

# Rozwiązanie układu równań Ax = b
x = gaussian_elimination_with_pivoting(A, b)
print("Rozwiązanie x:", x)

# determinant = np.linalg.det(matrix)


```