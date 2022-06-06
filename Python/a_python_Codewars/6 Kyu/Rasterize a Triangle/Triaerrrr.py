import math
import numpy as np

def draw_triangle(triangle, n):
    A, B, C = np.array(triangle[0]), np.array(triangle[1]), np.array(triangle[2])
    AB, AC = B - A, C - A
    BC, BA = C - B, A - B
    CA, CB = A - C, B - C
    val = []
    for y in range(n):
        arr = []
        for x in range(n):
            xy = np.array([x, y])
            v1 = xy - A
            v2 = xy - B
            v3 = xy - C

            a1 = calculate_angle(v1,v2)
            a2 = calculate_angle(v2,v3)
            a3 = calculate_angle(v3,v1)
            angle = a1 + a2 + a3
            if (x, y) == A == B == C:
                arr.append(1)
            elif round(angle,3) == round(2*math.pi,3):
                arr.append(1)
            else:
                arr.append(0)
        val.append(arr)
    return val
def calculate_angle(V1,V2):
    unit_vector_1 = V1 / np.linalg.norm(V1)
    unit_vector_2 = V2 / np.linalg.norm(V2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    return np.arccos(dot_product)
triangle = ((2,1), (0, 3), (5, 4))
print(draw_triangle(triangle, 6))

# SkalarA = round(sum(AB * AC), 1)
# SkalarB = round(sum(BC * BA), 1)
# SkalarC = round(sum(CA * CB), 1)
#
# skalar_list = [SkalarA, SkalarB, SkalarC]
# vinkelA = round(degrees(acos(SkalarA / (lengde(AB) * lengde(AC)))))
# vinkelB = round(degrees(acos(SkalarB / (lengde(BC) * lengde(BA)))))
# vinkelC = round(degrees(acos(SkalarC / (lengde(CA) * lengde(CB)))))
# vinkel_list = sorted((vinkelA, vinkelB, vinkelC))