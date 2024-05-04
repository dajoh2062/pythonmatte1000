import numpy as np
import sympy as sp
import matplotlib as plt
def f(x):
    return x**3+6*x+9

a=0
b=5
n=200
areal=0
dx=(b-a)/n

while(a<b):
    a=a+dx
    areal+=(f(a)*dx)

print(areal)