import numpy as np
import sympy as sp

n = int(input("Matrix dimension: "))
A_list = []

for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter element {i+1}/{j+1}: "))
        row.append(element)
    A_list.append(row)

A = np.array(A_list)

B_list=[]
for k in range(n):
    row=[]
    element=int(input(f"Enter element {k+1}/1: "))
    row.append(element)
    B_list.append(row)

print("------------------------------")
print("Mellomregning: ")
B=np.array(B_list)
print("\nMatrise A:")
sp.pprint(A)
print("\nMatrise B:")
sp.pprint(B)



total = np.hstack((A, B))

# Printing the result

print("\nTotalmatrise Ax=b:")
sp.pprint(total)


print("\nTotalmatrise på redusert trappeform: ")
rref_total=np.array(sp.Matrix(total).rref()[0])
print(rref_total)



det_rref_total = np.linalg.det(A)
print(f"\nDeterminant: {round(det_rref_total,3)}")


print("------------------------------")
if(det_rref_total!=0):
    print("Totalmatrisen har en entydig løsning")
    x_vektor=[]
    for i in range (n):
        x_verdi=rref_total[i,-1]
        print(f"x{i}={x_verdi}")
        x_vektor.append([x_verdi])
    x_vektor=np.array(x_vektor)
    print(f"\nXvektoren blir da:\n {x_vektor}")


else:
    print("Totalmatrisen har enten uendlige eller ingen løsning")
