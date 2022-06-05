import numpy as np
from math import sqrt


def area(vec1, vec2, vec3) -> object:
    return 1 / 2 * abs(vec1[0] * (vec2[1] - vec3[1]) + vec2[0] * (vec3[1] - vec1[1]) + vec3[0] * (vec1[1] - vec2[1]))


def lengde(vektor) -> float:
    return sqrt(vektor[0] ** 2 + vektor[1] ** 2)


def isInside(vec1, vec2, vec3, P) -> bool:
    # Calculate area of triangle ABC
    Areal = area(vec1, vec2, vec3)

    # Calculate area of triangle PBC
    A1 = area(P, vec2, vec3)

    # Calculate area of triangle PAC
    A2 = area(vec1, P, vec3)

    # Calculate area of triangle PAB
    A3 = area(vec1, vec2, P)

    # Check if sum of A1, A2 and A3
    # is same as A
    if (Areal == (A1 + A2 + A3)):
        return True
    else:
        return False

def Bresenham(triangle, n) -> list:
    A, B, C = np.array(triangle)
    x1, x2, x3 = A[0], B[0], C[0]
    y1, y2, y3 = A[1], B[1], C[1]

    # Driver program to test above function
    # Let us check whether the point P(10, 15)
    # lies inside the triangle formed by
    # A(0, 0), B(20, 0) and C(10, 30)

    # This code is contributed by Danish Raza
    AB = B - A
    BC = C - B
    CA = A - C
    print((1 / 3) * (A + B + C))
    lst = []
    OA = lengde(A)
    OB = lengde(B)
    OC = lengde(C)
    print(OA, OB, OC)
    area = (1 / 2) * abs(OA * OB + OB * OC + OC * OA)
    shoelace = 1 / 2 * abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    print("are ", area)
    print("sho ", shoelace)
    for y in range(n):
        arr = []
        for x in range(n):
            xy = np.array([x, y])
            v1 = xy - A
            v2 = xy - B
            v3 = xy - C
            # print(f"xy: {xy}\n V1: {v1} V2: {v2} V3: {v3}")
            if (xy == A).all() or (xy == B).all() or (xy == C).all():
                arr.append('1')
            elif isInside(A, B, C, xy):
                arr.append('1')
            else:
                arr.append('0')
        lst.append(arr)
    return '\n'.join([(str(i)) for i in lst])


triangle = ((2,1), (0, 3), (5, 4))
print(Bresenham(triangle, 6))
