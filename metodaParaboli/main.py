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

