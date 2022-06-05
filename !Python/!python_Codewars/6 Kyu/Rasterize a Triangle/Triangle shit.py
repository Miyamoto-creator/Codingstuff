import math
import numpy as np
import timeit as t

def draw_triangle(triangle, n):
    A, B, C = triangle
    val = []
    for y in range(n):
        arr = []
        for x in range(n):
            xy = np.array([x, y])
            v1 = np.subtract(xy, A, dtype=float)
            v2 = np.subtract(xy, B, dtype=float)
            v3 = np.subtract(xy, C, dtype=float)

            a1 = calculate_angle(v1, v2)
            a2 = calculate_angle(v2, v3)
            a3 = calculate_angle(v3, v1)
            angle = a1 + a2 + a3
            if (x,y) == A or (x,y) == B or (x,y) == C:
                arr.append(1)
            else:
                if np.round(angle, 10) == np.round(2*math.pi, 10):
                    arr.append(1)
                else:
                    arr.append(0)
        val.append(arr)
    return '\n'.join([(str(i)) for i in val])
def calculate_angle(a, b):
    v1, v2 = a / np.linalg.norm(a), b / np.linalg.norm(b)
    dot_product = np.dot(v1, v2)
    return np.arccos(dot_product)


triangle = [(2, 1), (0, 3), (5, 4)]
print(draw_triangle(triangle, 6))
print("Run time:", t.timeit(lambda: draw_triangle(triangle, 6), number=10000))

triangle = [(1, -49997), (2, 3), (3, 50002)]
print(draw_triangle(triangle, 6))
print("Run time:", t.timeit(lambda: draw_triangle(triangle, 6), number=10000))