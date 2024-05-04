import numpy as np
import matplotlib.pyplot as plt
import cmath

def f(x):
    return 4*(x**3)-2*x

x_values=[]
y_values=[]
h=0.5
for i in np.arange (-3.0, 3.0, 0.1):
    dy=(f(i+h)-f(i))/h
    print(f"{round(dy,6)}, ")
    x_values.append(i)
    y_values.append(dy)

plt.plot(x_values,y_values, label="f'(x)")
plt.plot(x_values, 12*(np.array(x_values) ** 2) - 2, label="12x^2 - 2")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('Plot of the derivative of f(x)')
plt.legend()
plt.grid(True)
plt.show()