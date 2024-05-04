import numpy as np
import matplotlib.pyplot as plt
import cmath

i=1j

#y=int(input("Imaginærdel: "))
#x=int(input("Realdel: "))
#n=int(input("Eksponent: "))

x=4
y=3
n=3

def radians (thetha):
    thetha_2= thetha/np.pi
    return (f"{round(thetha_2,4)}π")


z_kartesisk = x+y*1j
print(f"Kartesisk form: z^{n} = {z_kartesisk}")

thetha=np.arctan(y/x)
r=np.sqrt(x**2+y**2)

z_polar=r*(np.cos(thetha)+1j*np.sin(thetha))
print(f"Polarform: z^{n} = {round(r,2)}(cos{radians(thetha)}+1j*sin{radians(thetha)})")

z_kompleks=r*np.exp(thetha*1j)
print(f"Kompleks form: z^{n} = {round(r,2)}*e^({radians(thetha)}*1j)")

print(f"Thetha = {thetha}, {radians(thetha)}")

thetha_2= thetha/np.pi

print("\n")
for k in range(n):
    w_kartesisk = r ** (1 / n) * np.exp(1j * (thetha / n + 2 * np.pi * k / n))

    print(f"Root {k + 1}: {np.round(w_kartesisk,3)},  {round(r,2)}^1/{n}*e^(i*{radians(thetha / n + 2 * np.pi * k / n)})")
