import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 6*x + 9

a = 0
b = 5
n = 200
areal = 0
dx = (b - a) / n

while a < b:
    areal += (f(a) + f(a + dx)) * dx / 2
    a += dx

print(areal)
