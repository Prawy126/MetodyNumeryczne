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
