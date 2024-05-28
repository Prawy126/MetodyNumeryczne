from sympy import symbols, expand, linsolve, Matrix

# Definicja zmiennych i węzłów
x = symbols('x')
punkty_x = [0, 3, 6, 9, 12]
punkty_y = [4, 5, 4, 1, 2]
stopien = 3

# Inicjalizacja list
macierz_row = []
wektor_col = []

# Tworzenie macierzy i wektora
for x_i, y_i in zip(punkty_x, punkty_y):
    row = [x_i**k for k in range(stopien + 1)]
    macierz_row.append(row)
    wektor_col.append(y_i)

# Konwersja list na obiekty Matrix
macierz = Matrix(macierz_row)
wektor = Matrix(wektor_col)

# Rozwiązanie układu równań metodą najmniejszych kwadratów
coefficients = linsolve((macierz.T * macierz, macierz.T * wektor))

# Wyodrębnienie współczynników
coefficients = list(coefficients.args[0])

# Tworzenie wielomianu aproksymującego
wielomian = sum(c * x**i for i, c in enumerate(coefficients))

# Wypisanie wyniku
print("Wielomian aproksymujący (m = 3):", expand(wielomian).evalf())
