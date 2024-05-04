import matplotlib.pyplot as plt
import numpy as np

#definerer funksjon f, og g som den deriverte av x som vi fant analytisk
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    return np.exp(-x/4)*((-1/4)*np.arctan(x) + 1/(x**2+1))

#bruker bisectionmethod/halveringsmetode for å finne nullpunktet.
#funkjsonen vil da dele opp gitt intervall i 2, for å så videre dele intervallet #som inneholder nullpunktet i 2 igjen, helt til feilen er mindre enn 1e-5

def bisection(funk, a, b):
    if funk(a) * funk(b) >= 0:
        print("Ingen eller flere enn 1 rot i intervallet")
        return None

    while abs(b - a) > 1e-5:
        c = (b + a) / 2

        if funk(c) == 0:
            print(f"x=: {c}")
            print(f"feilen er: {abs(b - a)}")
            return c

        elif funk(c) * funk(a) < 0:
            b = c
        else:
            a = c

    print(f"x={c}")
    print(f"feilen er : {abs(b - a)}")
    print(f"g(x) = {g(c)}")
    return c



rot = bisection(g, -10, 10)

#plotter funksjonene og nullpunktet i samme plot
x_verdier = np.linspace(-20, 20, 400)
y_verdier_f = f(x_verdier)
y_verdier_g = g(x_verdier)

plt.plot(x_verdier, y_verdier_f, label="f(x)")
plt.plot(x_verdier, y_verdier_g, label="g(x)")

plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.title("f(x) og g(x)")
plt.legend()

plt.scatter(rot, g(rot), color='red', label='Rot', zorder=5)
plt.grid(True)
plt.show()

