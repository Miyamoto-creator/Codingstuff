

from numpy import array
from math import sqrt, acos, degrees

x1 = float(1)
y1 = float(4)
# x1 = float(input("Gi x-verdi til punkt a: "))
# y1 = float(input("Gi y-verdi til punkt a: "))

x2 = float(-1)
y2 = float(4)
# x2 = float(input("Gi x-verdi til punkt b: "))
# y2 = float(input("Gi y-verdi til punkt b: "))

x3 = float(0)
y3 = float(2)
# x3 = float(input("Gi x-verdi til punkt c: "))
# y3 = float(input("Gi y-verdi til punkt c: "))

A = array([x1, y1])
B = array([x2, y2])
C = array([x3, y3])

# VEKTORER
AB = B - A
AC = C - A

BA = A - B
BC = C - B

CA = A - C
CB = B - C
# side_a = sqrt(x1 ** 2 + y1 ** 2)
# side_b = sqrt(x2 ** 2 + y2 ** 2)
# side_c = sqrt(x3 ** 2 + y3 ** 2)

lengde_AB = round(sqrt(AB[0] ** 2 + AB[1] ** 2), 1)
lengde_AC = round(sqrt(AC[0] ** 2+ AC[1] ** 2), 1)

lengde_BC = round(sqrt(BC[0] ** 2 + BC[1] ** 2), 1)
lengde_BA = round(sqrt(BA[0] ** 2 + BA[1] ** 2), 1)

lengde_CA = round(sqrt(CA[0] ** 2 + CA[1] ** 2), 1)
lengde_CB = round(sqrt(CB[0] ** 2 + CB[1] ** 2), 1)

def is_valid_triangle(side_a, side_b, side_c):
    print(side_a, side_b, side_c)
    if side_c == side_b == side_a:
        return "Punktene gir en Likesidet trekant"
    elif side_c == side_b:
        return "Punktene gir en Likebeinet trekant"
    elif side_a + side_b >= side_c:
        return "Punktene gir en Trekant, men den er hverken likesidet eller likebeinet"
    else:
        return "Punktene gir ikke en trekant"

print(is_valid_triangle(lengde_AB, lengde_BC, lengde_AC))