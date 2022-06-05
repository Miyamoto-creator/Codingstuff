import random
import numpy as np

n = 6
m = []
for y in range(n):
    arr = []
    for x in range(n):
        arr.append(0)
    m.append(arr)



def flood_recursive(matrix):
    A = np.array([2, 1])
    B = np.array([0, 3])
    C = np.array([5, 4])
    triangle = A, B, C
    def Bresenham(triangle, n) -> list:
        mid = (1 // 3) * (A + B + C)
        return mid
    width = len(matrix)
    height = len(matrix[0])

    def fill(x, y, start_color, color_to_update):
        # if the square is not the same color as the starting point
        if matrix[x][y] != start_color:
            return
        # if the square is not the new color
        elif matrix[x][y] == color_to_update:
            return
        else:
            # update the color of the current square to the replacement color
            matrix[x][y] = color_to_update
            neighbors = [(x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1),
                         (x, y - 1), (x, y + 1)]
            for n in neighbors:
                if 0 <= n[0] <= width - 1 and 0 <= n[1] <= height - 1:
                    fill(n[0], n[1], start_color, color_to_update)

    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    start_color = matrix[start_x][start_y]
    fill(Bresenham(triangle, n)[0], Bresenham(triangle, n)[1], start_color, 1)
    return '\n'.join([i for i in list(map(str, matrix))])

A = np.array([2, 1])
B = np.array([0, 3])
C = np.array([5, 4])

triangle = A, B, C
print(flood_recursive(m))
