import sympy as sp

def f(x):
    return x * sp.exp(-x**2)

def g(x):
    return sp.exp(-x**2) - 2 * (x**2) * sp.exp(-x**2)

x_verdi = 0.50

for i in range(1, 50):
    x_verdi = x_verdi - f(x_verdi) / g(x_verdi)
    print(x_verdi)
