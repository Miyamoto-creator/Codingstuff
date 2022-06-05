from numpy import array
from math import sqrt, acos, degrees


# A
x_A = float(6)
y_A = float(0)

# B
x_B = float(1)
y_B = float(0)

# C
x_C = float(3.46)
y_C = float(0.02)

# SUMMER
A = array([x_A, y_A])
B = array([x_B, y_B])
C = array([x_C, y_C])

# VEKTORER
AB = B - A
AC = C - A

BA = A - B
BC = C - B

CA = A - C
CB = B - C

# SKALAR
SkalarA = sum(AB * AC)
SkalarB = sum(BC * BA)
SkalarC = sum(CA * CB)

# ABSOLUTT LENGDE
lengde_AB = sqrt(AB[0] ** 2 + AB[1] ** 2)
lengde_AC = sqrt(AC[0] ** 2+ AC[1] ** 2)

lengde_BC = sqrt(BC[0] ** 2 + BC[1] ** 2)
lengde_BA = sqrt(BA[0] ** 2 + BA[1] ** 2)

lengde_CA = sqrt(CA[0] ** 2 + CA[1] ** 2)
lengde_CB = sqrt(CB[0] ** 2 + CB[1] ** 2)


# VINKEL
vinkelA = degrees(acos(SkalarA / (lengde_AB * lengde_AC) ))
vinkelB = degrees(acos(SkalarB / (lengde_BC * lengde_BA) ))
vinkelC = degrees(acos(SkalarC / (lengde_CA * lengde_CB) ))

print(f"AB = {AB}\n"
      f"BC = {BC}\n"
      f"AC = {AC}\n"
      f"SkalarA = {SkalarA}\n"
      f"lengde AB = {lengde_AB}\n"
      f"lengde BA = {lengde_BA}\n"
      f"lengde BC = {lengde_BC}\n"
      f"lengde BA = {lengde_BA}\n"
      f"lengde AC = {lengde_AC}\n"
      f"VinkelA = {vinkelA}\n"
      f"VinkelB = {vinkelB}\n"
      f"VinkelC = {vinkelC}\n"
      f"Sum av vinklel A, B og C = {vinkelA + vinkelB + vinkelC}")


# vinkelB = degrees(acos(SkalarB / (lengde_BC * lengde_BA) ))
# vinkelC = degrees(acos(SkalarC / (lengde_CA * lengde_CB) ))