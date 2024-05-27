from sympy import symbols, expand, linsolve, Matrix

# Aproksymacja wielomianowa.
# Węzły P1(0,4), P2(3,5), P3(6,4), P4(9,1), P5(12,2).

# Wzór aproksymacji wielomianowej (metoda najmniejszych kwadratów):
# Węzły x_1, x_2, ..., x_n
# Wzór S_n(x) = E i=1/n | [y_i - y(x_i)]^2
# Gdzie y_i = f(x_i)

x = symbols('x')
punkty_x = [0, 3, 6, 9, 12]  # Wartości 'x' dla danych węzłów
punkty_y = [4, 5, 4, 1, 2]  # Wartości 'y' dla danych węzłów
stopien = 3  # Stopień wielomianu aproksymującego

macierz = []
wektor = []

# Tworzenie macierzy i wektora wyników
for x_i, y_i in zip(punkty_x, punkty_y):
    # Tworzenie wiersza macierzy dla każdego punktu x_i
    wiersz = [x_i ** k for k in range(stopien + 1)]
    macierz.append(wiersz)
    wektor.append(y_i)

# Konwersja list na macierz równań i wektor wyników
macierz = Matrix(macierz)
wektor = Matrix(wektor)

# Metoda najmniejszych kwadratów
wspolczynniki = linsolve((macierz.T * macierz, macierz.T * wektor))  # linsolve -  rozwiązuje układ równań liniowych.

wspolczynniki = list(wspolczynniki.args[0])

# Tworzenie wielomianu aproksymującego
wielomian = sum(c * x ** i for i, c in enumerate(wspolczynniki))
# enumerate(wspolczynniki) - funkcja odpowiedzialna za iteracje przez listę współczynników, która zwraca pary (indeks, współczynnik).

# Wynik
print("Wielomian aproksymujący (dla m = 3):", expand(wielomian).evalf())
