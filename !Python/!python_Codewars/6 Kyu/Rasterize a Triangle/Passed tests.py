import numpy as np


def draw_triangle(triangle, n) -> list:
    A, B, C = np.array(triangle)
    lst = []
    for y in range(n):
        arr = []
        for x in range(n):
            xy = np.array([x, y])
            if (xy == A).all() or (xy == B).all() or (xy == C).all():
                arr.append(1)
            elif isInside(A, B, C, xy):
                arr.append(1)
            else:
                arr.append(0)
        lst.append(arr)
    return lst


def area(vec1, vec2, vec3) -> object:
    return 1 / 2 * abs(vec1[0] * (vec2[1] - vec3[1]) + vec2[0] * (vec3[1] - vec1[1]) + vec3[0] * (vec1[1] - vec2[1]))


def isInside(vec1, vec2, vec3, P) -> bool:
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
