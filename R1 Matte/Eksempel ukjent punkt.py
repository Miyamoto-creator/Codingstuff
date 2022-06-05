"Eksempel ukjent punkt"
import numpy as np

"Koordinater til punktet A"
x_A = float(input("Gi x-verdien til punktet A: "))
y_A = float(input("Gi y-verdien til punktet A: "))

"Koordinater til punktet B"
x_B = float(input("Gi x-verdien til punktet B: "))
y_B = float(input("Gi y-verdien til punktet B: "))

"Koordinater til punktet C"
x_C = float(input("Gi x-verdien til punktet C: "))
y_C = float(input("Gi y-verdien til punktet C: "))

"""
OD-Vektoren vil være lik som koordinatet til D
Vil derfor finne OD-Vektor 
Dette kan gjøres ved å gå kjente vektorer.
Først OA og deretter AD"""

OA = np.array([x_A, y_A])
BC = np.array([x_C - x_B, y_C - y_B])
AD = BC

OD = OA + AD

print(f"D-koordinatet er: ({OD[0]}, {OD[1]})")