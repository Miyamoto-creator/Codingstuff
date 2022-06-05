from math import acos, degrees, sqrt
import matplotlib.pyplot as plt
from random import randint
from numpy import array

plt.axes()

points = (
    array((4, 8)),
    array((7.46, 8)),
    array((4, 10)),
)

# points = (
#     array((randint(0, 20), randint(0, 20))),
#     array((randint(0, 20), randint(0, 20))),
#     array((randint(0, 20), randint(0, 20))),
# )

# A, B, C = points

# x_1 = A[0]
# x_2 = B[0]
# x_3 = C[0]
# y_1 = A[1]
# y_2 = B[1]
# y_3 = C[1]
Likebeinet = []
Trekant = []
Likesidet = []
spesiell = []
likebeinet_og_rettvinklet = []
rettvinklet = []


def triangle_check(A, B, C):
    print(A, B, C)
    #Plotter trekanten slik at du kan se hvordan hver av dem ser ut
    lineA = plt.Line2D((A[0], B[0]), (A[1], B[1]), lw=2.5)
    plt.gca().add_line(lineA)
    lineB = plt.Line2D((B[0], C[0]), (B[1], C[1]), lw=2.5)
    plt.gca().add_line(lineB)
    lineC = plt.Line2D((A[0], C[0]), (A[1], C[1]), lw=2.5)
    plt.gca().add_line(lineC)
    plt.axis('scaled')
    plt.show()

    def lengde(vektor):
        return sqrt(vektor[0] ** 2 + vektor[1] ** 2)
    AB, AC = B - A, C - A
    BC, BA = C - B, A - B
    CA, CB = A - C, B - C

    # Skalarer for hver side av trekanten.
    SkalarA = round(sum(AB * AC), 1)
    SkalarB = round(sum(BC * BA), 1)
    SkalarC = round(sum(CA * CB), 1)


    vektor_list = set([lengde(i) for i in (AB, BC, AC)])
    # print(vektor_list)
    # print("AB = ",AB, " BC = " ,BC, " AC = ", AC)
    # print("L(AB) = ",lengde(AB), " L(BC) = " ,lengde(BC), " L(AC) = ", lengde(AC))
    x = []
    y = []
    skalar_list = [SkalarA, SkalarB, SkalarC]
    vinkelA = round(degrees(acos(SkalarA / (lengde(AB) * lengde(AC)))))
    vinkelB = round(degrees(acos(SkalarB / (lengde(BC) * lengde(BA)))))
    vinkelC = round(degrees(acos(SkalarC / (lengde(CA) * lengde(CB)))))
    vinkel_list = sorted((vinkelA, vinkelB, vinkelC))
    print(skalar_list, vinkel_list, vektor_list)
    for i, (n, k) in enumerate(points):
        x.append(n)
        y.append(k)
    if len(set(x)) == 1 or len(set(y)) == 1:
        return "Punktene gir ikke en trekant"
    else:
        if 60 in vinkel_list and len(set(vinkel_list)) == 1:
            return "Punktene gir en likesidet trekant"
        elif 90 and 60 and 30 in vinkel_list:
            return "Punktene gir en 90, 60, 30 graders trekant"
        elif len(vektor_list) == 2 and 0 in skalar_list:
            return "Punktene gir en Likebeinet og rettvinklet trekant"
        elif 0 in skalar_list:
            return "Punktene gir en rettvinklet trekant"
        elif len(vektor_list) == 2:
            return "Punktene gir en Likebeinet trekant"
        else:
            return "Punktene gir en Trekant, men den er hverken likesidet eller likebeinet"

nitti, seksti, tretti = (4, 8), (7.46, 8), (4, 10) # 90, 60, 30 trekant
rettvinklet, og, likebeint = (-1, 4), (1, 4), (1, 2)
li, ke, sidet = (1, 4), (-1, 4), (0, 2.27)
lik, e, beint = (), (), ()
tre, ka, nt = (), (), ()
# print(triangle_check(array((4, 8)), array((7.46, 8)), array((4, 10))))
print(triangle_check(array(nitti), array(seksti), array(tretti)))
print(triangle_check(array(rettvinklet), array(og), array(likebeint)))

lst = []
for i, n in enumerate(range(100)):
    points = (
        array((randint(0, 20), randint(0, 20))),
        array((randint(0, 20), randint(0, 20))),
        array((randint(0, 20), randint(0, 20))),
    )
    D, E, F = points
    print(triangle_check(D, E, F))

print(triangle_check(array(li), array(ke), array(sidet)))
print(Likesidet)