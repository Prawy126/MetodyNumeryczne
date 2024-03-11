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


# Przykład użycia z funkcją lambda
try:
    root = bisekcja(lambda x: x**3+x-1, 0, 1, 0.01)
    print(f"Przybliżony pierwiastek to: {root}")
except ValueError:
    print("Założenia nie zostały spełnione")

