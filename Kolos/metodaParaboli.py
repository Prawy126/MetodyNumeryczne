import sympy as sp

# Definicja symboli i funkcji
x = sp.symbols('x')


def metoda_simpsona(f_expr, a, b, n):
    if n % 2 != 0:
        raise ValueError("Liczba przedziałów musi być parzysta.")

    # Szerokość każdego przedziału (podstawa paraboli)
    h = (b - a) / n

    f_a = f_expr.subs(x, a)
    f_b = f_expr.subs(x, b)

    result = f_a + f_b
    odd_sum = sum(f_expr.subs(x, a + k * h) for k in range(1, n, 2))
    even_sum = sum(f_expr.subs(x, a + k * h) for k in range(2, n, 2))
    result += 4 * odd_sum + 2 * even_sum
    result *= (h / 3)

    # Obliczenie czwartej pochodnej funkcji jeśli liczba przedziałów jest większa od 1 i kiedy stopień wielomianu
    # jest większy lub równy 4
    if sp.total_degree(f_expr) >= 4:
        f_x_pochodna4 = sp.diff(f_expr, x, 4)
        blad = ((b - a) * h ** 4 / 180) * f_x_pochodna4.subs(x, b)
    else:
        blad = None

    return result.evalf(), blad.evalf() if blad else None


# Testowanie funkcji
if __name__ == "__main__":
    # Przedział [a,b]
    a_val = -3
    b_val = 1
    n_val = 10000  # Liczba podziałów

    # f(x)
    f_expr = sp.sin(x) * sp.exp(-3 * x) + x ** 3

    # Wywołanie
    try:
        wynik, blad = metoda_simpsona(f_expr, a_val, b_val, n_val)
        print(f"Wynik całki metodą Simpsona: {wynik:.10f}")  # Zaokrąglenie do 10 miejsc po przecinku
        print(f"Szacowany błąd metody: {blad:.10f}" if blad else "Nie można obliczyć błędu")
        # Obliczenie całki dokładnie dla porównania
        calka_dokladna = sp.integrate(f_expr, (x, a_val, b_val))
        print(f"Dokładny wynik całki: {calka_dokladna.evalf()}")
    except ValueError as e:
        print(e)