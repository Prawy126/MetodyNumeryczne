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

