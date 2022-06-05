import numpy as np
import math


triangle = ((2,1), (0, 3), (5, 4))

def draw_triangle(triangle, n):
    A, B, C = np.array(triangle[0]), np.array(triangle[1]), np.array(triangle[2])
    AB, AC = B - A, C - A
    BC, BA = C - B, A - B
    CA, CB = A - C, B - C
    vectors = [AB, AC, BC, BA, CA, CB]
    val = []
    def calculate_angle(V1, V2):
        unit_vector_1 = V1 / np.linalg.norm(V1)
        unit_vector_2 = V2 / np.linalg.norm(V2)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        return np.arccos(dot_product)
    def SameSide(p1, p2, a, b):
        cp1 = np.cross(b - a, p1 - a)
        cp2 = np.cross(b - a, p2 - a)
        if np.dot(cp1, cp2) >= 0:
            return 1
        else:
            return 0
    def PointInTriangle(p, a, b, c):
        if SameSide(p, a, b, c) and SameSide(p, b, a, c) and SameSide(p, c, a, b):
            return 1
        else:
            return 0
    for y in range(n):
        arr = []
        for x in range(n):
            v1 = np.subtract((x, y), A)
            v2 = np.subtract((x, y), B)
            v3 = np.subtract((x, y), C)

            a1 = calculate_angle(v1, v2)
            a2 = calculate_angle(v2, v3)
            a3 = calculate_angle(v3, v1)
            angle = a1 + a2 + a3
            if (x, y) == A or (x, y) == B or (x, y) == C:
                arr.append(1)
            else:
                if round(angle, 3) == round(2 * math.pi, 3):
                    arr.append(1)
                else:
                    arr.append(0)
            val.append(arr)
    return val




print(draw_triangle(triangle, 6))