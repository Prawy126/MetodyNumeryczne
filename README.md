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
