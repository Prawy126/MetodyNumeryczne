# Definiujemy współrzędne punktów
x0, y0 = 1, 5
x1, y1 = 2, 7
x2, y2 = 3, 6


# Funkcja do mnożenia dwóch wielomianów
def multiply_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result


# Funkcja do dodawania dwóch wielomianów
def add_poly(poly1, poly2):
    length = max(len(poly1), len(poly2))
    result = [0] * length
    for i in range(len(poly1)):
        result[i] += poly1[i]
    for i in range(len(poly2)):
        result[i] += poly2[i]
    return result


# Współczynniki wielomianów bazowych L0, L1, L2
L0_num = multiply_poly([-x1, 1], [-x2, 1])
L0_den = (x0 - x1) * (x0 - x2)
L0 = [coef / L0_den for coef in L0_num]

L1_num = multiply_poly([-x0, 1], [-x2, 1])
L1_den = (x1 - x0) * (x1 - x2)
L1 = [coef / L1_den for coef in L1_num]

L2_num = multiply_poly([-x0, 1], [-x1, 1])
L2_den = (x2 - x0) * (x2 - x1)
L2 = [coef / L2_den for coef in L2_num]

# Mnożenie wielomianów L0, L1, L2 przez odpowiednie y0, y1, y2
P0 = [coef * y0 for coef in L0]
P1 = [coef * y1 for coef in L1]
P2 = [coef * y2 for coef in L2]

# Dodawanie wielomianów P0, P1, P2 w celu uzyskania końcowego wielomianu P
P = add_poly(add_poly(P0, P1), P2)

# Wyświetlenie wyniku
print("Współczynniki wielomianu interpolacyjnego Lagrange’a:", P)


# Funkcja do wypisania wielomianu w czytelnej formie
def print_polynomial(poly):
    terms = []
    for i, coef in enumerate(poly):
        if coef != 0:
            if i == 0:
                terms.append(f"{coef}")
            elif i == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{i}")
    print(" + ".join(terms))


print("Wielomian interpolacyjny Lagrange’a: ", end="")
print_polynomial(P)

""""
Definicja współrzędnych punktów: x0, y0 = 1, 5, x1, y1 = 2, 7, x2, y2 = 3, 6.
Funkcja multiply_poly: Mnoży dwa wielomiany reprezentowane przez listy współczynników.
Funkcja add_poly: Dodaje dwa wielomiany reprezentowane przez listy współczynników.
Obliczenia wielomianów bazowych L0, L1, L2: Liczone są współczynniki wielomianów bazowych.
Mnożenie L0, L1, L2 przez odpowiednie y0, y1, y2: Uzyskujemy części składowe wielomianu interpolacyjnego.
Dodawanie wielomianów P0, P1, P2: Sumujemy składowe, aby uzyskać końcowy wielomian interpolacyjny.
Wyświetlenie wyniku: Funkcja print_polynomial wypisuje wielomian w czytelnej formie.
"""

"""
from sympy import symbols, expand

# Definiujemy zmienną symboliczną
x = symbols('x')

# Punkt (x0, y0) = (1, 5), (x1, y1) = (2, 7), (x2, y2) = (3, 6)
x0, x1, x2 = 1, 2, 3
y0, y1, y2 = 5, 7, 6

# Wielomiany bazowe Lagrange'a
L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

# Wielomian interpolacyjny Lagrange'a
P = expand(y0 * L0 + y1 * L1 + y2 * L2)

# Wyświetlenie wyniku
print("Wielomian interpolacyjny Lagrange’a:", P)
"""
